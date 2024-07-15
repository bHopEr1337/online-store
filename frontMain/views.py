from django.shortcuts import render
from frontMain.models import Product
from django.core.paginator import Paginator


def index(request):
    return render(request, template_name='frontMain/index.html', context={
        'products' : Product.objects.all()
    })

def about(request):
    return render(request, template_name='frontMain/about.html')

def contact(request):
    return render(request, template_name='frontMain/contact.html')

def house(request):
    post_list = Product.objects.all()
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)
    houses = paginator.page(page_number)

    return render(request, template_name='frontMain/house.html', context={
        'houses' : houses
    })

def price(request):
    return render(request, template_name='frontMain/price.html')
