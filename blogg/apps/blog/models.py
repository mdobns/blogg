from django.db import models
from apps.auths.models import UserProfile

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50)
    author = models.ForeignKey(UserProfile, related_name="posts", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def add_post(self, title, content):
        post = Post(title=title, content=content, published=True)
        post.save()
        return post

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, blank=True, null=True, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'