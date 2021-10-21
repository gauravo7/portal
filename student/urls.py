from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about,name="about"),
    path('html',views.html,name="html"),
    path('form',views.form,name="form"),
    path('form2',views.form2,name="form2"),
    path('page',views.page,name="page"),
]