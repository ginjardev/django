from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    return render(
        request,
        'blog/home.html',
        {
            "posts": Post.objects.all()
        }
    )

def about(request):
    return render(
        request,
        'blog/about.html'
    )