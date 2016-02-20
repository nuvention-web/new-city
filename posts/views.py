from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

# Create your views here.
def home(request):
    context = {}
    return render(request, 'facebookjssdk.html', context)

def post_create(request):
    return HttpResponse("<h1>Hello World</h1>")

def post_detail(request):
    return HttpResponse("<h1>Hello World</h1>")

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request,'index.html', context)

def post_update(request):
    return HttpResponse("<h1>Hello World</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello World</h1>")

