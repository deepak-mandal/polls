from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

from django.template import loader

# Create your views here.

##################################################
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.urls import reverse


'''
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=', '.join([q.question_text for q in latest_question_list])
    template=loader.get_template('polls/index.html')
    context={'latest_question_list': latest_question_list,
    
    }
    
    return HttpResponse(template.render(context, request))
    #return HttpResponse('Hello, world. You are at the polls index.')
    
def details(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})
    #return HttpResponse('You are looking at question %s.' % question_id)

'''

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    

def results(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
    #response='You are looking at the results of question %s.'
    #return HttpResponse(response % question_id)

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice.', })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #Always return HttpResponseRediredct after successfully dealing with POST data
        #This prevent data from being posed twice if a user hits back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    



    #return HttpResponse('You are voting on question %s.' % question_id)
