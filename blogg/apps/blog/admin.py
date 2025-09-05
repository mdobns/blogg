from django.contrib import admin
from .models import UserProfile, Post, Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
