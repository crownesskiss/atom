from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models  import Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ',  '.join([q.question_text for q in  lastest_question_list])
    return HttpResponse(output)
    return HttpResponse("hello world")
def detail(request, question_id):
    return HttpResponse("you are looking question?%s" % question_id)

def results(request, question_id):
    response = "你正在看问题的%s 的结果"
    return HttpResponse("you are looking %s results" % question_id)
def vote(request, question_id):
    return HttpResponse("您在问题%s 上的投票" % question_id)
