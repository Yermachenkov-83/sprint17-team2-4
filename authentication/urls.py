from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='users'),
    path('users/<int:user_id>', detail, name='user'),
    path('create', create, name='create'),
    path('edit/<int:user_id>', edit, name='edit'),
    path('delete/<int:user_id>', delete_user, name='delete'),

]