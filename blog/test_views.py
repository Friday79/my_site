from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category, Subscriber
from blog.forms import CommentForm 
from django.contrib.messages import get_messages


class PostViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=self.user,
            status=1,
            category=self.category
        )
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Post')
        
    def test_post_detail_get_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_post_upvote_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('post_upvote', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
    
    

    def test_post_downvote_view(self):
        self.client.login(username='testuser', password='password123')
        self.post.likes.add(self.user)
        response = self.client.post(reverse('post_downvote', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_post_comment_submission(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('post_detail', args=[self.post.slug]), {
            'body': 'A test comment',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your comment was submitted successfully.')
        self.assertEqual(self.post.comments.count(), 1)

    def test_post_like_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists()) 

    def test_post_detail_ajax_vote_upvote(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'action': 'upvote'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['upvotes'], 1)


class SubscribeViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('subscribe')  # make sure your URL name is 'subscribe'

    def test_subscribe_valid_email(self):
        """Test subscribing a new email successfully"""
        response = self.client.post(self.url, {'email': 'test@example.com'}, follow=True)
        self.assertTrue(Subscriber.objects.filter(email='test@example.com').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Thank you for subscribing!", [str(m) for m in messages])
        self.assertRedirects(response, reverse('home'))

    

    def test_subscribe_invalid_email(self):
        """Test subscribing with an invalid email"""
        response = self.client.post(self.url, {'email': 'invalid-email'}, follow=True)
        self.assertFalse(Subscriber.objects.filter(email='invalid-email').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Please enter a valid email address.", [str(m) for m in messages])
        self.assertRedirects(response, reverse('home'))

    
class UnsubscribeViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('unsubscribe')  # make sure your URL name is 'unsubscribe'
        self.subscriber = Subscriber.objects.create(email='test@example.com')

    def test_unsubscribe_existing_email(self):
        """Test unsubscribing an existing email"""
        response = self.client.post(self.url, {'email': 'test@example.com'}, follow=True)
        self.assertFalse(Subscriber.objects.filter(email='test@example.com').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("test@example.com has been unsubscribed successfully.", [str(m) for m in messages])
        self.assertRedirects(response, reverse('home'))

    def test_unsubscribe_nonexistent_email(self):
        """Test unsubscribing a non-existent email"""
        response = self.client.post(self.url, {'email': 'nonexistent@example.com'}, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("This email is not in our subscriber list.", [str(m) for m in messages])
        self.assertRedirects(response, reverse('home'))

    def test_unsubscribe_get_request(self):
        """Test GET request renders unsubscribe page"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'unsubscribe.html')
        self.assertEqual(response.status_code, 200)
