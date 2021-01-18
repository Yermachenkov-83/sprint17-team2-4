from django.shortcuts import render, redirect

from .models import *


def index(request):
    users = CustomUser.objects.order_by('last_name')
    return render(
        request,
        'authentication/index.html',
        {'title': 'Посетители Библиотеки', 'users': users}
    )

def detail(request, user_id):
    user = CustomUser.get_by_id(user_id)
    context = {
        'title': f'Пользователь номер: {user.id}',
        'user': user
    }

    return render(
        request,
        'authentication/detail.html',
        context
    )


