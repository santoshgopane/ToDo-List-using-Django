from django.shortcuts import render,redirect
from .models import List
from .forms import Listform
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework import viewsets
from .serializers import todoserializer
from django.contrib.auth.models import auth,User
from . import forms
from django.http import HttpResponse


def Home(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        user = request.user
        addto = List(item=item,user=user)
        addto.save()
        all_item = List.object.all()
        messages.success(request,('Item has been added Successfully!'))
        return render(request,'index.html',{'all_item':all_item})
        # else:
            # return HttpResponse('I dont Know dfaq is happening!')
    else:
        # return HttpResponse('I dont Knoow!')
        all_item = List.object.all()
        return render(request,'index.html',{'all_item':all_item})
        # return render(request,'index.html')

def register(request):
    # if request.method == 'POST':
    if request.method == 'POST':
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        username = request.POST['username']
        # first_name = request.POST['email']
        password = request.POST['psw']
        re_password = request.POST['psw-repeat']
        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!')
                return redirect('register')
            # elif User.objects.filter(email=mail).exists():
            #     messages.info(request,'Email Taken!')
            #     return redirect('reg')
            else:   
                user_create = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                user_create.save()
                messages.info(request,'User Created!')
                return redirect('login')
        else:
            messages.info(request,'Password Not matching!')
            return redirect('register')

    return render(request,'Registration.html')

def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['pwd']

        User = auth.authenticate(username=Username,password=Password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,'Incorrect Credentials!')
            return redirect('login')
    return render(request,'login.html')


def delete(request,list_id):
    item = List.object.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been Deleted!'))
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('/')