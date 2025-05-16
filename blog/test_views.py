from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category
from blog.forms import CommentForm  # Only needed if you want to test form validity


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
        response = self.client.get(reverse('home'))  # Ensure 'post_list' matches your urls.py name
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
        self.assertEqual(response.json()['likes_count'], 1)
    
    

    def test_post_downvote_view(self):
        self.client.login(username='testuser', password='password123')
        self.post.likes.add(self.user)
        response = self.client.post(reverse('post_downvote', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['likes_count'], 0)

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
        