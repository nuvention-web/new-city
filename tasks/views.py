from django.shortcuts import render

# Create your views here.
def index(request, question_id):
    categories = Category.objects.all()
    return HttpResponse("You're looking at question %s." % question_id)

def selected(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)