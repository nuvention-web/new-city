from django.shortcuts import render
from django.core.urlresolvers import reverse
from posts.forms import CityForm, UserProfileForm
from posts.models import City
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

    return render(request, 'HP.html', context)


def user_profile_detail(request, user_profile_id= None):
    user_profile = get_object_or_404(UserProfile, id=user_profile_id)

    context = {
            "user_profile": user_profile,
            }

    return render(request, "user_profile.html", context)


def create_user_profile(request):
    form = UserProfileForm(request.POST or None)
    print("form",form)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.save()
        return HttpResponseRedirect(reverse('user_profile_detail',
                                    kwargs={'user_profile_id': user_profile.id}))
    context = {
        "form": form,
    }
    return render(request, "create_user_profile.html", context)
