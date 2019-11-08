from django.urls import path

from . import views

urlpatterns = [
    path('menu/get-all/', views.get_all_menu, name='get_menu'),
    path('menu/post/', views.post_menu, name='post_menu'),
    path('menu/delete/', views.delete_all_menu, name='delete_all_menu'),
    path('order/post/', views.post_order, name='post_order'),
    path('order/get/', views.get_order, name='get_order'),
    path('order/get-all/', views.get_all_order, name='get_all_order'),
    path('order/delte/', views.delete_all_order, name='delete_all_order'),
]