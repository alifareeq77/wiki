from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path('create', views.create_new_page, name='create'),
    path('<titles>', views.title, name='title')

]