from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Post, Category, Comment, Subscriber

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.user,
            category=self.category,
            content="This is a test post.",
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name="Test Commenter",
            email="test@example.com",
            body="This is a test comment.",
            approved=True,
        )
        # Subscriber setup
        self.subscriber = Subscriber.objects.create(email="subscriber@example.com")

    # --- Existing model tests ---
    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_comment_str(self):
        self.assertEqual(str(self.comment), f"Comment {self.comment.body} by {self.comment.name}")

    def test_post_total_votes(self):
        self.post.upvotes = 5
        self.post.downvotes = 2
        self.assertEqual(self.post.total_votes(), 3)

    def test_post_number_of_likes(self):
        self.post.likes.add(self.user)
        self.assertEqual(self.post.number_of_likes(), 1)

    # --- Subscriber model tests ---
    def test_subscriber_str(self):
        """__str__ should return the subscriber email"""
        self.assertEqual(str(self.subscriber), "subscriber@example.com")

    def test_subscriber_unique_email(self):
        """Creating a subscriber with duplicate email should raise IntegrityError"""
        with self.assertRaises(IntegrityError):
            Subscriber.objects.create(email="subscriber@example.com")

    def test_subscriber_created_on_auto_now_add(self):
        """created_on should be automatically set"""
        self.assertIsNotNone(self.subscriber.created_on)
