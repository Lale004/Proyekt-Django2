from django.shortcuts import render
from .models import Post,Comment

def index_view(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'posts': posts,
        'comments': comments
    }
    return render(request, 'index.html', context)

# Create your views here.
