from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.homepage import Homepage
from .views.sproduct import sproduct
from .views.about import About
from .views.contact import Contact 
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.wishlist import Wishlist
from .views.search import Search
from .middlewares.auth import auth_middleware




urlpatterns = [
    path('',Homepage.as_view(),name='index'),
    path('shop',auth_middleware(Index.as_view()), name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name = 'login'),
    path('logout',logout,name = 'logout'),
    path('/cart',Cart.as_view(),name='cart'),
    path('check-out',CheckOut.as_view(),name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()),name='orders'),
    path('sproduct/<int:myid>/',sproduct.as_view(),name='sproduct'),
    path('about',About.as_view(),name='about'),
    path('contact',Contact.as_view(),name='contact'),
    path('wishlist',auth_middleware(Wishlist.as_view()),name='wishlist'),
    path('search', Search.as_view(), name='search')
    
]
