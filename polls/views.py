from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404


from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Choice, Question

def index(request):
    # displays the latest 5 poll questions in the system, separated by commas, according to publication date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # page that displays the question text for a given poll
     question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
