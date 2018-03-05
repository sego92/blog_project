from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles/index.html', {'posts':posts})

def detail(request):
    return render(request, 'articles/detail.html', {'posts':posts})

def delete(request):
    return render(request, 'articles/delete.html', {'posts':posts})

def create(request):
    return render(request, 'articles/create_modify.html', {'posts':posts})

def modify(request):
    return render(request, 'articles/create_modify.html', {'posts':posts})