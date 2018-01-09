# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import  vegetables,NonVeg,Dairy
from ymarchome.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    dict={'one':'comeone'}
    return render(request,"homepages/home.html")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('ymarchome:index'))


def veg(request):
    vegtab=vegetables.objects.all()
    dict={'records':vegtab}
    return render(request,"homepages/veg.html",dict)

def nonveg(request):
    nonvegtab=NonVeg.objects.all()
    dict={'records':nonvegtab}
    return render(request,"homepages/nonveg.html",dict)

def dairy(request):
    dairy=Dairy.objects.all()
    dict={'records':dairy}
    return render(request,"homepages/dairy.html",dict)


def register(request):
    registered= False
    if request.method == "POST" :
        user_form=UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else :
            print user_form.errors
    else :
        user_form=UserForm()


    return render(request,'homepages/registation.html',{"user_form":user_form,'registered':registered})



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('ymarchome:index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'homepages/login.html', {'invalid':"invalid logins provided"})

    else:
        #Nothing has been provided for username or password.
        return render(request, 'homepages/login.html', {})


def forgot(request):
    return render(request, 'homepages/forgot.html')
