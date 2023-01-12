from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month_number>/', views.month_view, name='calendar_month'),
    path('actual/', views.show_current_month, name='current_month'),
]
