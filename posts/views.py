import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# from .forms import PostForm, HouseForm
from .forms import HouseForm
from .models import Post
# from .models import Post, UserProfile

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
    post_list = Post.objects.all()
    # user_list = Post.get_user.objects.all()
    # user = post_list.user.all()

    # for post in post_list:
    #     user = post_list[post].get_user()

    context = {
        # "user" : user, 
        "post_list" : post_list, 
    }
    return render(request,'post_list.html', context)

def post_update(request):
    return HttpResponse("<h1>Hello World</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello World</h1>")

def create_user(request):
    print ("this is request *************")
    print (request.POST)
    if request.method == 'POST':
        post_text = request.POST.get('user')
        response_data = {}
        print("this is post text *********")
        print(post_text)

        # post = Post(text=post_text, author=request.user)
        # post.save()

        # response_data['result'] = 'Create post successful!'
        # response_data['postpk'] = post.pk
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
