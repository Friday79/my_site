from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import Post, Category
from .forms import CommentForm


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

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was submitted successfully.')
        else:
            messages.error(request, 'There was a problem submitting your comment.')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Handles upvote/downvote actions via AJAX"""
        post = get_object_or_404(Post, slug=slug)

        action = request.POST.get('action')
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
            post.likes.add(request.user)
        return JsonResponse({"success": True, "likes_count": post.likes.count()})


class PostDownvote(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        if request.user.is_authenticated:
            post.likes.remove(request.user)
        return JsonResponse({"success": True, "likes_count": post.likes.count()})


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
