from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.coupon import Coupon
from .models.contact import Query


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','status']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

    

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order,AdminOrder)
admin.site.register(Query)
admin.site.register(Coupon)


