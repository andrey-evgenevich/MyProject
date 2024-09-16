from django.shortcuts import render


def home(reqwest):
    return render(reqwest, 'catalog/templates/home.html')


def contacts(reqwest):
    return render(reqwest, 'catalog/contacts.html')
