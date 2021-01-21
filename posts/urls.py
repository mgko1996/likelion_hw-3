from django.urls import path
from .views import new, create, main, show

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('/show/<int:id>', show, name="show"),
]