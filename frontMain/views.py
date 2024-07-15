from django.shortcuts import render
from frontMain.models import Product


def index(request):
    return render(request, template_name='frontMain/index.html', context={
        'products' : Product.objects.all()
    })

def about(request):
    return render(request, template_name='frontMain/about.html')

def contact(request):
    return render(request, template_name='frontMain/contact.html')

def house(request):
    return render(request, template_name='frontMain/house.html', context={
        'products' : Product.objects.all()
    })

def price(request):
    return render(request, template_name='frontMain/price.html')
