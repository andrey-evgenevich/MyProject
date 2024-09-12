from django.shortcuts import render


def home(reqwest):
    return render(reqwest, 'home.html')


def contacts(reqwest):
    return render(reqwest, 'contacts.html')
