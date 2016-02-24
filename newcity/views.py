from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

def home(request):
    context = {}
    return render(request, 'main.html', context)