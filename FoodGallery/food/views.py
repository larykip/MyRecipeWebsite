from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def foodposts(request):
    return render(request, 'receipe-post.html')