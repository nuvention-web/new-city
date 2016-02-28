from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import CityForm
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
