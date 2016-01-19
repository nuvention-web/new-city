from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Category, Task



# Create your views here.
def index(request):
    categories = Category.objects.all()
    template = loader.get_template('tasks/index.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def selected(request):
    selectedCategories = Category.objects.filter(selected = False)
    response = "selected"
    return HttpResponse(response)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)