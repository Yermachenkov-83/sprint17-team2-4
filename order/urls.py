from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='orders'),
    path('<int:order_id>', detail, name='order'),
    ]