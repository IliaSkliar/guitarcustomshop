from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import date, timedelta

from orders.forms import OrderCreateForm
from orders.models import Order


# Create your views here.
@login_required
def orders_list(request):
    orders = Order.objects.filter(owner=request.user)
    if request.user.is_master:
        orders = Order.objects.filter(master=request.user)
    open_orders = Order.objects.filter(status=Order.STATUS_OPEN)
    return render(request, 'orders.html',
                  context={'orders': orders, 'open_orders': open_orders, })


@login_required
def create_order(request):
    form = OrderCreateForm()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.owner = request.user
            order.save()
            return HttpResponseRedirect(reverse('orders'))

    return render(request, 'create_order.html', context={'form': form})


@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order_details.html', context={'order': order})


@login_required
def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status != order.STATUS_OPEN:
        error = 'Order is not open'
        return render(request, 'order_details.html',
                      context={'order': order, 'error': error})
    if not request.user.is_master:
        error = 'You have no permissions'
        return render(request, 'order_details.html',
                      context={'order': order, 'error': error})
    order.status = order.STATUS_IN_WORK
    order.master = request.user
    order.save()
    return HttpResponseRedirect(reverse('orders'))

@login_required
def order_done(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status != order.STATUS_IN_WORK:
        error = 'Order must be in work'
        return render(request, 'order_details.html',
                      context={'order': order, 'error': error})
    if not request.user.is_master and order.master != request.user:
        error = 'You have no permissions'
        return render(request, 'order_details.html',
                      context={'order': order, 'error': error})
    order.status = order.STATUS_DONE
    order.master = request.user
    order.warranty = date.today()+timedelta(days=30*6)
    order.save()
    return HttpResponseRedirect(reverse('orders'))
