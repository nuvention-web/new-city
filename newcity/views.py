from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse
from posts.forms import CityForm, UserProfileForm
from posts.models import City, UserProfile, UserProfileTag, Tag
import json
#from django.contrib.formtools.wizard.views import SessionWizardView
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect



# Create your views here.
def home(request, initial_city=None):
    form = CityForm(request.GET or None)
    city_list = City.objects.all()
    print(request.GET)

    if form.is_valid():

        initial_city = request.GET.get('initial_city')

        if 'searching_for_home' in request.GET:
            return HttpResponseRedirect(reverse('posts:list',
                                            kwargs={'initial_city': initial_city}))

        elif 'searching_for_roommate' in request.GET:
            return HttpResponseRedirect(reverse('posts:list_roommate',
                                            kwargs={'initial_city': initial_city}))
    else:
        if 'searching_for_home' in request.GET:
            return HttpResponseRedirect(reverse('posts:list'))

        elif 'searching_for_roommate' in request.GET:
            return HttpResponseRedirect(reverse('posts:list_roommate'))

    context = {
        "city_list" : city_list,
    }

    return render(request, 'landing.html', context)


def user_profile_detail(request, user_profile_id= None):
    user_profile = get_object_or_404(UserProfile, pk=user_profile_id)
    user_tag_instance = UserProfileTag.objects.filter(user_profile = user_profile)
    print(user_tag_instance)

    context = {
            "user_profile": user_profile,
            "user_tag_instance": user_tag_instance,
            }

    return render(request, "user_profile.html", context)


def create_user_profile(request):
    user = request.user
    social_accounts = user.socialaccount_set.all()
    account = social_accounts[0]
    picture = account.get_avatar_url()
    data = account.extra_data
    tag_list = request.POST.getlist("tags")
    print(tag_list)

    # UserProfile
    gender = data.get('gender')
    if gender == 'male':
        gender = 'M'
    else:
        gender = 'F'
    # later
    fb_count = data.get('friends').get('summary').get('total_count')
    friends = data.get('friends').get('data') # array of querydict

    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.gender = gender
        user_profile.user = user
        user_profile.save()

        for tag in tag_list:
            tag_instance = Tag.objects.get(id=int(tag))
            new_usertag = UserProfileTag(user_profile = user_profile, tag=tag_instance)
            new_usertag.save()

        return HttpResponseRedirect(reverse('user_profile_detail',
                                    kwargs={'user_profile_id': user_profile.pk}))
    context = {
        "form": form,
    }
    return render(request, "create_user_profile.html", context)
