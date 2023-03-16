from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product

class Wishlist(View):
    def get(self,request):
        if request.session.get('wishlist') == None:
            return render(request,'wishlist.html')
            
        ids = (list(request.session.get('wishlist').keys()))
        products = Product.get_products_by_id(ids)
        return render(request,'wishlist.html',{'products':products})