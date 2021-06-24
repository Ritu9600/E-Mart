from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class Comments(View):
   def get(self, request):
        return render(request, 'comments.html')
