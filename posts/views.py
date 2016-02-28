from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse
from .forms import HouseForm, PostForm, FilterRoommateForm, CityForm
from .models import Post, House, PostTag, Tag, UserProfile, City
import json
#from django.contrib.formtools.wizard.views import SessionWizardView
from formtools.wizard.views import SessionWizardView

# Create your views here.
def home(request):
    form = CityForm(request.GET or None)
    if form.is_valid():
        initial_city = request.GET.get('initial_city')

        if 'searching_for_home' in request.GET:
            return HttpResponseRedirect(reverse('posts:list',
                                        kwargs={'initial_city': initial_city}))

        elif 'searching_for_roommate' in request.GET:
            return HttpResponseRedirect(reverse('posts:list_roommate',
                                        kwargs={'initial_city': initial_city}))

    context = {}
    return render(request, 'HP.html', context)

def post_create_house(request):

    form = HouseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Succesfully Created")
        #return redirect("create_post")
        return HttpResponseRedirect(reverse('posts:create_post',
                                    kwargs={'house_id': instance.id}))
    context = {
        "form": form,
    }
    return render(request, "create_house.html", context)

def post_create_post(request, house_id=None):
    house_instance = get_object_or_404(House, id=house_id)
    form = PostForm(request.POST or None)
    if form.is_valid() and house_instance:
        instance = form.save(commit=False)
        id_tag_list = request.POST.getlist('tags')
        instance.house = house_instance
        instance.save()

        post_instance = instance
        for id_tag in id_tag_list:
            tag_instance = Tag.objects.get(id=int(id_tag))
            print(type(tag_instance))
            print(type(house_instance))
            new_posttag = PostTag(post=post_instance, tag=tag_instance)
            new_posttag.save()

        return redirect("posts:list_roommate")
    # else:
    #     messages.error(request, "Not Successfully Created")

    context = {
        "form": form,
    }
    return render(request, "create_post.html", context)

def post_detail(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)

    context = {
            "title": instance.title,
            "instance": instance,
            }
    return render(request, "post_detail.html", context)

def post_list(request):
# def post_list(request, initial_city=None):
    # init_city_query = City.objects.filter(name=initial_city)
    # post_list = Post.objects.filter(city=init_city_query)
    post_list = Post.objects.all()

    # post_list.filter()

    tag_list = Tag.objects.all()
    # user_list = Post.get_user.objects.all()
    # user = post_list.user.all()

    # for post in post_list:
    #     user = post_list[post].get_user()

    context = {
        # "user" : user,
        "post_list" : post_list,
        "tag_list" : tag_list,
    }
    return render(request,'post_list.html', context)

def post_list_roommate(request):
    roommate_list = UserProfile.objects.all()
    form = FilterRoommateForm(request.GET or None)

    if request.is_ajax():
        gender = request.GET.get('gender')
        hometown = request.GET.get('hometown')

        if gender:
            roommate_list = roommate_list.filter(gender = gender)
        if hometown:
            city_instance = City.objects.get(name = hometown)
            roommate_list = roommate_list.filter(hometown = city_instance)

    context = {
        "roommate_list": roommate_list,
        "form": form,
    }
    return render(request, 'post_list_roommate.html', context)


def post_update(request):
    return HttpResponse("<h1>Hello World</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello World</h1>")

def login(request):
    context = {}
    return render(request, 'login.html', context)

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

class QuestionnaireWizard(SessionWizardView):
    template_name = "questionnaire.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(self, form_list)

        return render_to_response('done.html', {'form_data':form_data})

def process_form_data(self, form_list):
    form_data = [form.cleaned_data for form in form_list]

    school = form_data[0]['school']
    hometown = form_data[1]['hometown']
    job = form_data[2]['job']

    #hometown must be a city instance
    hometown_instance = City.objects.get(name = hometown)

    print(self.request.user)
    new_user_profile = UserProfile(user=self.request.user, school = school, hometown = hometown_instance, job = job)
    new_user_profile.save()

    return form_data


