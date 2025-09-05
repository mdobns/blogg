from django.shortcuts import render
from .models import Post

# Create your views here.
def homepage(request):
    blog = Post.objects.filter(published = True)

    return render(request, 'homepage.html', {'blog': blog})