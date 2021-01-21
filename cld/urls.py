from django.urls import path
from . import views


app_name = 'cld'
urlpatterns = [
    path('', views.calendar, name="calendar"),
]