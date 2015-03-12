from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Questions


# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse("Your're looking at question %s." % question_id)

def result(request, question_id):
	response = "You're looking at the result og question %s."

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
