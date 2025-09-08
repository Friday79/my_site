from django.test import TestCase
from .models import Comment, Post, Category, Subscriber
from .forms import CommentForm, PostForm, CategoryForm, SubscriberForm
from django.contrib.auth.models import User

class TestForms(TestCase):

    def setUp(self):
        # Set up user and category for PostForm
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    # -------- CommentForm Tests --------
    def test_comment_form_valid_data(self):
        form = CommentForm(data={'body': 'This is a test comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors)

    # -------- PostForm Tests --------
    def test_post_form_valid_data(self):
        form_data = {
            'title': 'Test Post',
            'slug': 'test-post',
            'category': self.category.id,
            'featured_image': '',
            'excerpt': 'This is an excerpt',
            'content': 'This is content',
            'status': 1
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_invalid_data(self):
        form_data = {
            'title': '',
            'slug': '',
            'category': '',
            'featured_image': '',
            'excerpt': '',
            'content': '',
            'status': ''
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('slug', form.errors)
        self.assertIn('category', form.errors)

    # -------- CategoryForm Tests --------
    def test_category_form_valid_data(self):
        form = CategoryForm(data={'name': 'New Category'})
        self.assertTrue(form.is_valid())

    def test_category_form_invalid_data(self):
        form = CategoryForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    # -------- SubscriberForm Tests --------
    def test_subscriber_form_valid_data(self):
        form = SubscriberForm(data={'email': 'subscriber@example.com'})
        self.assertTrue(form.is_valid())
        subscriber = form.save()
        self.assertEqual(subscriber.email, 'subscriber@example.com')

    def test_subscriber_form_invalid_email(self):
        form = SubscriberForm(data={'email': 'invalid-email'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)