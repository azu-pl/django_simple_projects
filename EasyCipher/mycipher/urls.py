from django.urls import path
from . import views


urlpatterns = [
    path('cipher/code/rotn/<int:n>/<str:slug>/', views.rotn_code, name='code_rotn'),
    path('cipher/decode/rotn/<int:n>/<str:slug>/', views.rotn_decode, name='decode_rotn'),
    path('cipher/code/adbash/<str:slug>/', views.adbash_coded, name='code_adbash'),
]