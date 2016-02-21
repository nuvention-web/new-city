from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    context = {}
    return render(request, 'facebookjssdk.html', context)

def post_create_house(request):

    form = HouseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Succesfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successfully Created")

    context = {
        "form": form,
    }
    return render(request, "post_create.html", context)

def post_create_post(request):
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

