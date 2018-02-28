from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles/index.html', {'posts':posts})

def detail(request):
    pass

def delete(request):
    pass

def create(request):
    pass

def modify(request):
    pass