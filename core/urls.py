from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, shop, signup, myaccount, edit_myaccount
from product.views import product, remove_review, edit_review

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    path('shop/<slug:slug>/remove_review/', remove_review, name='remove_review'),
    path('shop/<slug:slug>/edit_review/', edit_review, name='edit_review'),
]