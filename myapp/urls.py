from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [   
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('my-account/',views.myaccount,name='my-account'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('seedlings/',views.seedlings,name='seedlings'),
    path('indigenous-seeds/',views.indigenous_seeds,name='indigenous-seeds'),
    path('books/',views.books,name='books'),
    path('other_products/',views.other_products,name='other_products'),
    path('outgrowers/',views.outgrowers,name='outgrowers'),
    path('services/',views.services,name='services'),
    path('clients_projects/',views.clients_projects,name='clients_projects'),
    path('natural_treatment/',views.natural_treatment,name='natural_treatment'),
    path('edible_weeds/',views.edible_weeds,name='edible_weeds'),
    path('fruit_growing/',views.fruit_growing,name='fruit_growing'),
    path('plant_disease_treatment/',views.plant_disease_treatment,name='plant_disease_treatment'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact_us/',views.contact_us,name='contact_us'),





]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)