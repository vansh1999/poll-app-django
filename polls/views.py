from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]

    context = {
        'latest_question_list_key': latest_question_list,
    }
    return render(request , 'polls/index.html' , context)



def detail(request , question_id):
    question_front_end = get_object_or_404(Question , pk = question_id)
    return render(request , 'polls/detail.html' , {'question_key' : question_front_end})


def results(request , question_id):
    response = "you are looking at results of question %s. "
    return HttpResponse(response % question_id)

def vote(request ,  question_id):
    return HttpResponse("you are voting at question %s."  % question_id)




