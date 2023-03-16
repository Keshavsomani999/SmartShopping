from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Homepage(View):
    def get(self,request):
        FeatureProduct = Product.objects.all()[:8]
        NewArrival = Product.objects.all().order_by('-id')[:8]
        return render(request,'Homepage.html',{'FeatureProduct':FeatureProduct,'NewArrival':NewArrival})
