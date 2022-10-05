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

]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)