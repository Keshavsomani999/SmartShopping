from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
import random

class sproduct(View):
    def get(self,request,myid):
        product = Product.objects.filter(id=myid)

        items = list(Product.objects.all())
        FeaturedProduct = random.sample(items,4)
        return render(request,'sproduct.html',{'product':product[0],'FeaturedProduct':FeaturedProduct})