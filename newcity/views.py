from django.shortcuts import render
from django.core.urlresolvers import reverse
from posts.forms import CityForm
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
