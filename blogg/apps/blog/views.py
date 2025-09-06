from django.shortcuts import render
from .models import Post

# Create your views here.
def homepage(request):
    blog = Post.objects.filter(published = True)

    return render(request, 'homepage.html', {'blog': blog})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})