from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
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
        self.index_url = reverse("index")
        self.post_detail_url = reverse("post_detail", kwargs={"slug": self.post.slug})
        self.category_url = reverse("category_posts", kwargs={"slug": self.category.slug})

    def test_post_list_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "This is a test post.")

    def test_post_like_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("post_like", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 302)  # Redirect after like
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    def test_post_upvote_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("post_upvote", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.upvotes, 1)

    def test_post_downvote_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("post_downvote", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.downvotes, 1)

    def test_category_post_list_view(self):
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category_posts.html")
        self.assertContains(response, "Test Post")
