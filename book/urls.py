from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books'),
    path('<int:book_id>', views.detail, name='book'),
]
