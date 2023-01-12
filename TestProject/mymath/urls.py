from django.urls import path
from . import views

urlpatterns = [
    path('math/', views.welcome, name='welcome'),
    path('add/<int:a>/<int:b>/', views.add, name='add'),
    path('sub/<int:a>/<int:b>/', views.subtraction, name='subtraction'),
    path('div/<int:a>/<int:b>/', views.division, name='division'),
    path('multi/<int:a>/<int:b>/', views.multiply, name='multiply'),
]