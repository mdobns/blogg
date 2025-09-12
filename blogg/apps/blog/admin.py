from django.contrib import admin
from .models import  Post, Comments
from apps.auths.models import UserProfile
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published', 'view_count')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('author', 'text')
    ordering = ('-created_at',)

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
