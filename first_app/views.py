from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

# def index(request):
#     name = "Tolani"
#     return render(request, 'index.html', context={"name": name})

def index(request):
    return HttpResponse('Hello world')


def redirect(request):
    return HttpResponseRedirect(reverse('my_app:hello'))


# def hello(request):
#     return HttpResponse("Hello world")
#
#
# def helloo(request, name: str):
#     return HttpResponse(f"{name.title()}, welcome to Django")
