from django.shortcuts import render
from quiz.models import Quiz


# Create your views here.


def quiz(request):
    object = Quiz.objects.all()
    return render(request, 'main.html', {'questions': object})
