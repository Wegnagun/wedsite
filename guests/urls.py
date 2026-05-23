from django.urls import path

from . import views

app_name = 'guests'

urlpatterns = [
    path('', views.guest_answer, name='guests'),
]