from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Orders

# Create your views here.
def index(request):
    orders = Orders.objects.all()
    template = loader.get_template("ordersapp/index.html")
    context = {
        'orders_all' : orders
    }
    return HttpResponse(template.render(context, request))