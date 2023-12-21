from django.shortcuts import render, redirect
from .models import *
from .forms import *


def menu(request):
    eat = Eat.objects.all()
    return render(request, 'menu.html', context={'eat': eat})


def order(request):
    order = Order.objects.all()
    return render(request, 'order.html', context={'order':order})


def create(request):
    if request.method == "POST":
        form = AddEat(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            about = form.cleaned_data['about']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            Order.objects.create(title=title, about=about, price=price, category=category)
            return redirect('menu')
        else:
            form = AddEat()
            return render(request, 'create.html', context={'form': form})
    else:
        form = AddEat()
        return render(request, 'create.html', context={'form': form})


def delete(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return redirect('order')
    except:
        return redirect('order')
