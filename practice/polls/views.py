from django.shortcuts import render

# Create your views here.
from .models import Question, Choice, dummy
from django.http import HttpResponse


def index(request):
    lss = list(Question.objects.all().values())

    summa = {"hello": lss}
    return render(request, 'polls/index.html', summa)


def result(request, il):
    s = Choice.objects.filter(question_id=il)
    j = Question.objects.get(pk=il)

    return render(request, 'polls/choice.html', {'super': s, 'question_name': j})


def vote(request, val):
    j = Choice.objects.filter(question_id=val)
    k = Question.objects.get(pk=1).question_text

    return render(request, 'polls/vote.html', {'votelist': j, 'name': k})


def yes(request):
    id = request.POST['re']
    k = Choice.objects.filter(pk=id)[0].votes

    Choice.objects.filter(pk=id).update(votes=k + 1)
    il = Choice.objects.get(pk=id).question_id
    return result(request, il)
