from django.contrib import admin
from .models import Post, Comment, Category, Subscriber
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'upvotes', 'downvotes', 'total_votes')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['upvote_posts', 'downvote_posts']

    def upvote_posts(self, request, queryset):
        """Admin action to upvote selected posts."""
        for post in queryset:
            post.upvotes += 1
            post.save()
        self.message_user(request, "Selected posts have been upvoted.")

    upvote_posts.short_description = "Upvote selected posts"

    def downvote_posts(self, request, queryset):
        """Admin action to downvote selected posts."""
        for post in queryset:
            post.downvotes += 1
            post.save()
        self.message_user(request, "Selected posts have been downvoted.")

    downvote_posts.short_description = "Downvote selected posts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")  # Display category name and slug in the admin list view
    prepopulated_fields = {"slug": ("name",)}  # Automatically fill the slug field based on the name
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')  # show email and subscription date
    search_fields = ('email',)  # allow searching by email

