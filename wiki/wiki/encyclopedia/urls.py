from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('create', views.create_new_page, name='create'),
    path('random', views.random_page, name='random'),
    path('edit/<titl>', views.edit, name='edit'),
    path('<titles>', views.title, name='title'),

]
