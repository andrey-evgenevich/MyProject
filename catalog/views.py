from django.shortcuts import render


def home(reqwest):
    return render(reqwest, 'catalog/home.html')


def contacts(reqwest):
    return render(reqwest, 'contacts.html')
