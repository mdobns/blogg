from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("")  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'messages': messages})

    return render(request, 'login.html', {})

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'registration/signup.html')


@login_required(login_url='login')
def my_profile(request):
    user_posts = request.user.post_set.all()  # Get all posts by the user
    return render(request, 'my_profile.html', {'user_posts': user_posts})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('homepage')