from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from api.models import Menu, Order
from threading import Timer
import random

# Create your views here.
def get_all_menu(request):
    return HttpResponse(serializers.serialize('json', Menu.objects.all()), content_type='application/json')

def post_menu(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    image_url = request.GET.get('image_url')
    menu = Menu(name=name, price=price, image_url=image_url)
    menu.save()
    return HttpResponse(serializers.serialize('json',[menu,]), content_type='application/json')

def delete_all_menu(request):
    Menu.objects.all().delete()
    return HttpResponse(serializers.serialize('json', Menu.objects.all()), content_type='application/json')


def post_order(request):
    key = request.GET.get('key')
    menus = request.GET.get('menus')
    prices = request.GET.get('prices')
    counts = request.GET.get('counts')
    order = Order(key=key, menus=menus, prices=prices, counts=counts)
    order.save()
    t = Timer(random.uniform(10.0,20.0), change_status_order, [order])
    t.start()
    return HttpResponse(serializers.serialize('json',[order,]), content_type='application/json')

def change_status_order(order):
    print(order)
    print("change")
    order.done = True
    order.save()

def get_order(request):
    key = request.GET.get('key')
    order = Order.objects.get(key=key)
    return HttpResponse(serializers.serialize('json', [order,]), content_type='application/json')

def get_all_order(request):
    return HttpResponse(serializers.serialize('json', Order.objects.all()), content_type='application/json')

def delete_all_order(request):
    Order.objects.all().delete()
    return HttpResponse(serializers.serialize('json', Order.objects.all()), content_type='application/json')

