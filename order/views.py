from django.shortcuts import render, redirect

from .models import *


def index(request):
    orders = Order.objects.order_by('id')
    return render(
        request,
        'order/index.html',
        {'title': 'Заказы', 'orders': orders}
    )

def detail(request, order_id):
    order = Order.get_by_id(order_id)
    context = {
        'title': f'Номер заказа: {order.id}',
        'order': order
    }

    return render(
        request,
        'order/detail.html',
        context
    )
