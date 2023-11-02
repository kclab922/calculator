from django.shortcuts import render, redirect
from .models import Calculator

# Create your views here.

def index(request):
    quizzes = Calculator.objects.all()

    context = {
        'quizzes': quizzes
    }

    return render(request, 'index.html', context)


def history(request):
    quizzes = Calculator.objects.all()

    context = {
        'quizzes': quizzes
    }

    return render(request, 'history.html', context)


def new(request): 
    return render(request, 'new.html')


def check(request):
    # num1 = request.POST.get('num1')
    # num2 = request.POST.get('num2')
    # op = request.POST.get('op')
    # if op == '+':
    #     output = num1 + num2
    # elif op == 

    return render(request, 'check.html')

