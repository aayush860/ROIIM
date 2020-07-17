from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from cart.models import user_details,billing_details,configuration_key
from django.db import IntegrityError


def checkout(request):
    if request.user.is_authenticated:
        total_amount = (request.GET.get('cart_total',96))
        user_det = user_details.objects.get(username=request.user)
        billing_det = billing_details.objects.get(username=request.user)
        config = configuration_key.objects.get(id=1)
        return render(request, 'checkout.html', {'amount':total_amount,'user_det':user_det, 'billing_det':billing_det, 'config':config})

def windows(request):
    return render(request, 'window.html')

def logout(request):
    auth.logout(request)
    return redirect('/signin/')