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

def seedlings(request):
    return render (request, "seedlings.html")

def indigenous_seeds(request):
    return render (request, "indigenous-seeds.html") 

def books(request):
    return render (request, "books.html")

def other_products(request):
    return render (request, "other-products.html")

def outgrowers(request):
    return render (request, "outgrowers.html")

def services(request):
    return render (request, "services.html")

def clients_projects(request):
    return render (request, "client's-projects.html") 

def natural_treatment(request):
    return render (request, "natural-treatment.html")

def edible_weeds(request):
    return render (request, "edible-weeds.html")

def fruit_growing(request):
    return render (request, "fruit-growing.html")

def plant_disease_treatment(request):
    return render (request, "plant-disease-treatment.html")

def gallery(request):

    return render (request, "gallery.html")

def contact_us(request):

    return render (request, "contact-us.html")    