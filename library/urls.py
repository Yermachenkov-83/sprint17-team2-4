from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('book', include('book.urls')),
    path('author', include('author.urls')),
    path('order', include('order.urls')),
]
