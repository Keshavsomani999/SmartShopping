from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from django.db.models import Q


class Search(View):
    def post(self,request):
        search = request.POST.get('search')
        product = Product.objects.filter(Q(name__contains=search) | Q(category__name__icontains=search))
        return render(request, 'search.html', {'search':search,'product':product})
        