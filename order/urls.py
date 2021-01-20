from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='orders'),
    path('<int:order_id>', detail, name='order'),
    path('delete/<int:order_id>', delete_order, name='delete'),
    path('edit/<int:order_id>', edit_order, name='edit'),
    path('add', add_order, name='add'),
    ]