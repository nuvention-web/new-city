# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Category, Task
# from .forms import CategoryForm


# from mysite.polls.models import Poll, Choice
# from mysite.polls.forms import PollForm, ChoiceForm
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response

# def add_poll(request):
#     if request.method == "POST":
#         pform = PollForm(request.POST, instance=Poll())
#         cforms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice())
#         for x in range(0,3)]
#         if pform.is_valid() and all([cf.is_valid() for cf in cforms]):
#             new_poll = pform.save()
#             for cf in cforms:
#                 new_choice = cf.save(commit=False)
#                 new_choice.poll = new_poll
#                 new_choice.save()
#             return HttpResponseRedirect('/questions/')
#     else:
#         pform = PollForm(instance=Poll())
#         cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
#     return render_to_response('add_poll.html', {'poll_form': pform,
#                               'choice_forms': cforms})

# Create your views here.
def category_index(request):

    categories = Category.objects.all()

    context = {
        # 'form': form,
        'categories': categories,
    }
    return render(request, 'tasks/index.html', context)

# def selected(request):
#     selectedCategories = Category.objects.filter(selected = False)
#     response = "selected"
#     return HttpResponse(response)

# def question_index(request):
#     selectedCategories = Category.objects.get(category_selected = True)
#     context = {
#         'selectedCategories': selectedCategories
#     }
#     return render(request, 'tasks/question', context)

# def question(request):
#     pass

# def task(request):
#     selectedCategories = Category.objects.filter(selected = False)
#     response = "selected"
#     return HttpResponse(response)




# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# # ...
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
