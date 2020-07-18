from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from cart.models import user_details,billing_details,configuration_key
from django.db import IntegrityError


def checkout(request):
        if request.user.is_authenticated:
                print (request.POST['payload'])
                if request.POST.get('payload', -1)==-1:
                        return redirect('/window/')
                elif request.POST.get('firstName', -1)!=-1:
                        user_det = user_details.objects.filter(username=request.user).update(first_name=request.POST['firstName'], last_name=request.POST['lastName'], email=request.POST['email'], phone=request.POST['phone'], dob=request.POST['DOB'])
                        billing_det = billing_details.objects.filter(username=request.user).update(street=request.POST['address1'], street2=request.POST['address2'], city=request.POST['city'], zip_code=request.POST['zipcode'])
                    
                
                
                print (request.POST['payload'])
                user_det = user_details.objects.get(username=request.user)
                billing_det = billing_details.objects.get(username=request.user)
                config = configuration_key.objects.get(id=1)
                return render(request, 'checkout.html', {'amount':request.POST['payload'],'user_det':user_det, 'billing_det':billing_det, 'config':config})
        else:
                return redirect('/signin/')


def windows(request):
        if request.user.is_authenticated:
                return render(request, 'window.html')
        else:
                return redirect('/signin/')

def logout(request):
    auth.logout(request)
    return redirect('/signin/')



def payment_sucessful(request):
        if request.user.is_authenticated:
                return render(request, 'payment_sucessful.html')
        else:
                return redirect('/signin/')

def payment_unsucessful(request):
        if request.user.is_authenticated:
                return render(request, 'payment_unsucessful.html')
        else:
                return redirect('/signin/')

def payment_handle_not_created(request):
        if request.user.is_authenticated:
                return render(request, 'payment_handle_not_ceated.html')
        else:
                return redirect('/signin/')