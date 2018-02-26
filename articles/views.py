from django.shortcuts import render

# Create your views here.
def index(request):
    articles = [
        {'id': 1, 'title': 'First article', 'body': 'This is my first article'},
        {'id': 2, 'title': 'Second article', 'body': 'This is my second article'},
        {'id': 3, 'title': 'Third article', 'body': 'This is my third article'},
    ]
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, id):
    return render(request, 'articles/detail.html', {'id': id})