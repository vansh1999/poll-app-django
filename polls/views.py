from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question , Choice

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


def results(request, question_id):
    question_front = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question_back': question_front})

def vote(request, question_id):
    question_front_vote = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question_front_vote.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question_back': question_front_vote,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_front_vote.id,)))




