from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gear/add', views.add_gear, name='add_gear'),
]
