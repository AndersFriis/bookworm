from django.shortcuts import render

from django.htpp import HttpResponse



def index(request):
    return render(request, "core/index.html")

