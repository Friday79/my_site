from . import views
from django.urls import path
from .views import SubscribeView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('upvote/<slug:slug>', views.PostUpvote.as_view(), name='post_upvote'),
    path('downvote/<slug:slug>', views.PostDownvote.as_view(), name='post_downvote'),
    path('post/update/<slug:slug>', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryPostList.as_view(), name="category_posts"),
]
