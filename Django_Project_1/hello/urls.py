from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("sample", views.sample, name='sample'),
    path("<str:name>", views.greet, name='greet'),

    # path("<str:name>", views.greet, name='greet'),

    ]