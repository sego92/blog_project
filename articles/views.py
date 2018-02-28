from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html', {})

def detail(request, id):
    return render(request, 'articles/detail.html', {'id': id})