from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import Post, Category, Comment, Subscriber
from .forms import CommentForm, CategoryForm, PostForm, SubscriberForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
import requests



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6



class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "upvotes": post.upvotes,
                "downvotes": post.downvotes,
                "total_votes": post.total_votes(),
                "comment_form": CommentForm()
            },  
        )

    
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

    # Handle vote AJAX request
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            action = request.POST.get("action")
            if action == 'upvote':
                post.upvotes += 1
            elif action == 'downvote':
                post.downvotes += 1
            post.save()
            return JsonResponse({
                'upvotes': post.upvotes,
                'downvotes': post.downvotes,
                'total_votes': post.total_votes()
            })

    # Handle comment form
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = post.likes.filter(id=request.user.id).exists()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was submitted successfully.')
            commented = True
        else:
            messages.error(request, 'There was a problem submitting your comment.')
            commented = False

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": commented,
                "comment_form": comment_form,
                "liked": liked,
                "upvotes": post.upvotes,
                "downvotes": post.downvotes,
                "total_votes": post.total_votes(),
            },
        )



class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostUpvote(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        if request.user.is_authenticated:
            post.upvotes += 1
            post.save()
        return JsonResponse({
            "success": True,
            "upvotes": post.upvotes,
            "downvotes": post.downvotes,
            "total_votes": post.total_votes()
        })


class PostDownvote(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        if request.user.is_authenticated:
            post.downvotes += 1
            post.save()
        return JsonResponse({
            "success": True,
            "upvotes": post.upvotes,
            "downvotes": post.downvotes,
            "total_votes": post.total_votes()
        })

class CategoryPostList(View):
    """View for listing posts under a specific category"""
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(category=category, status=1).order_by("-created_on")

        return render(
            request,
            "category_posts.html",
            {
                "category": category,
                "posts": posts,
            },
        )
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = '/'          # redirect after save

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can edit

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


# Delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # redirect after delete

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = SubscriberForm   # make sure this is imported
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(self.request, " This email is already subscribed.")
        else:
            form.save()
            messages.success(self.request, " Thank you for subscribing!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, " Please enter a valid email address.")
        return super().form_invalid(form)
    
    

    

