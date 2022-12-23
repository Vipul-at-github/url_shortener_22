from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.mainfn, name='mainfn'),
    path('udhar', views.udhar, name='udhar'),
    path('<str:pk>', views.send),
]
