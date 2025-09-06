from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def homepage(request):
    blog = Post.objects.filter(published = True)

    return render(request, 'homepage.html', {'blog': blog})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'edit_post.html', {'post': post})

def edit_post_save(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'post_detail', post_id=post.id)