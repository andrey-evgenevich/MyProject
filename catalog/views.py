from django.shortcuts import render
from catalog.models import Product


def products_list(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, "product_list.html", context)


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")
