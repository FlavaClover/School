from django.shortcuts import render
from app.forms import LoginForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'app/index.html', context={'LoginForm': LoginForm})
