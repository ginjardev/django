from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(
        request,
        'blog/home.html',
        {
            "posts": Post.objects.all()
        }
    )


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'


def about(request):
    return render(
        request,
        'blog/about.html'
    )