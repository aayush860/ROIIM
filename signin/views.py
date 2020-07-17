from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from cart.models import user_details,billing_details
from django.db import IntegrityError


# Create your views here.
def signup(request):
    if request.method=='POST':
        fullname=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['pass']
        repeat_password=request.POST['repeat-pass']

        user=User.objects.create_user(username=username, email=email, password=password, first_name=fullname)
        user.save()

        user_det = user_details.objects.create(username=user, first_name='Aayush', last_name='Bhargava', email='xyz@gmail.com', phone='8602937010', dob='24/01/1996')
        user_det.save()

        billing_det = billing_details.objects.create(username=user, nick_name='Aayush', street='ejipura', street2='koramangala', city='bangalore', zip_code='458001', country='India', state='Karnataka')
        billing_det.save()
        
        return redirect('/window/')
    else:
        if request.user.is_authenticated:
            return redirect('/window/')
        return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/window/')
        else:
            return render(request, 'signin.html')
    else:
        if request.user.is_authenticated:
            return redirect('/window/')
        else:
            return render(request, 'signin.html')





