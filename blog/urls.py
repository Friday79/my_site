from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('upvote/<slug:slug>', views.PostUpvote.as_view(), name='post_upvote'),
    path('downvote/<slug:slug>', views.PostDownvote.as_view(), name='post_downvote'),
]
