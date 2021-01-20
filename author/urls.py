from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='authors'),
    path('/<int:author_id>', views.detail, name='author'),
    path('/add_author', views.add_author, name='add_author'),
]
