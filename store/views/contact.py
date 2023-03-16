from django.shortcuts import render,redirect
from django.views import View
from store.models.contact import Query

class Contact(View):
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        query = Query(name=name,email=email,subject=subject,message=message)
        query.placeQuery();
        return render(request,'contact.html')

    def get(self,request):
        return render(request,'contact.html')
    
    