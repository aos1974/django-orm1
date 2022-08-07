from contextlib import nullcontext
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'name':
        phones = Phone.objects.order_by('name').all()
    elif request.GET.get('sort') == 'min_price':
        phones = Phone.objects.order_by('price').all()
    elif request.GET.get('sort') == 'max_price':
        phones = Phone.objects.order_by('-price').all()
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug__startswith=slug)
    if len(phones) > 0:
        phone = phones[0]
    else:
        phone = nullcontext
    context = {
        'phone': phone,
    }
    return render(request, template, context)
 