from django.shortcuts import render

# Create your views here.

posts = [
    {
        "title": "New Blog Post",
        "author": "Khaleed",
        "published_date": "17th March, '22",
        "content": "This is an incredible content here"
    },
    {
        "title": "Another Blog Post",
        "author": "Azeez",
        "published_date": "16th March, '22",
        "content": "This is a brand new content here!"
    },
    {
        "title": "First Blog Post",
        "author": "Kareem",
        "published_date": "15th March, '22",
        "content": "A blog post with incredible content here"
    }
]

def home(request):
    return render(
        request,
        'blog/home.html',
        {
            "posts": posts
        }
    )

def about(request):
    return render(
        request,
        'blog/about.html'
    )