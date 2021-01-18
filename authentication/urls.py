from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='users'),
    path('/<int:user_id>', detail, name='user'),
]