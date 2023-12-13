from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import Items


# Create your views here
def index(request):
    item_list = Items.objects.all()
    output = ", ".join([i.ItemName for i in item_list])
    return HttpResponse(output)


def detail(request, item_code):
    return HttpResponse("You are looking at item no %s" % item_code)


def price(request, item_code):
    return HttpResponse(" You are looking at price of %s " % item_code)


def unit(request, item_code):
    return HttpResponse(" You are looking at unit of %s " % item_code)
