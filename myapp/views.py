from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, "index.html")

def about(request):
    return render (request, "about.html")

def cart(request):
    return render (request, "cart.html")

def checkout(request):
    return render (request, "checkout.html")

def myaccount(request):
    return render (request, "my-account.html")

def wishlist(request):
    return render (request, "wishlist.html")

def seadlings(request):
    return render (request, "seadlings.html")

def indigenous_seeds(request):
    return render (request, "indigenous_seeds.html") 

def books(request):
    return render (request, "books.html")

def other_products(request):
    return render (request, "other_products.html")