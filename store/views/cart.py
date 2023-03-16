from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.coupon import Coupon
from django.views import View
from store.models.product import Product

class Cart(View):
    
    def get(self,request):
        ids = (list(request.session.get('cart').keys()))
        if not ids:
            ids = {}
        products = Product.get_products_by_id(ids)
        return render(request,'cart.html',{'products':products})

    def post(self,request):
        ids = (list(request.session.get('cart').keys()))
        if not ids:
            ids = {}
        products = Product.get_products_by_id(ids)
        name = request.POST.get('coupon')
        sub_total = request.POST.get('sub_total')
        coupon = Coupon.get_coupon(name)
        if coupon:
            coupon_total_required = coupon.total_required
            if int(sub_total)>=coupon_total_required:
                return render(request,'cart.html',{"coupon":coupon,'products':products,'name':name})
            else:
                Add_more = coupon_total_required-int(sub_total)
                message = "Add more : "
                return render(request,'cart.html',{'products':products,'name':name,'message':message,'add_more':Add_more})
        return render(request,'cart.html',{"coupon":coupon,'products':products,'name':name})



    