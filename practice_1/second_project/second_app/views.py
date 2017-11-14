from django.shortcuts import render

# Create your views here.
import os


def index(request):
    directory = {'directory': os.path.curdir}
    return render(request, 'second_app/index.html', context=directory)
