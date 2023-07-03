from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import json

# Create your views here.
def home(request):
    return render(request,'home.html',{})
def index(request):
    return render(request,'myapp/index.html',{})

def navbar(request):
    return render(request,'myapp/navbar.html',{})

def userreg(request):
    return render(request,'myapp/userreg.html',{})

# for insertion
def insertuser(request):  
        data = json.loads(request.body)
        uid = data['uid']
        print("data value is", data)
        uname = data['uname']
        print("name is ", uname)
        uemail = data['uemail']
        ucontact = data['ucontact']
        us = User(uid=uid,uname=uname,uemail=uemail,ucontact=ucontact)
        us.save()
        return HttpResponse("record has been inserted")

def  updateuser(request):
    data = json.loads(request.body)
    r = data["uid"]
    print("value of r",r)
    user = User.objects.all()[r]  
    print("username",user.uname) 
    user.uname = "rajesh"
    print("upadted user name", user.uname)
    user.save();
    return HttpResponse("record has been updated")
    
def deleteuser(request):
    data = json.loads(request.body)
    r = data["uid"]
    # n=data["uname"]
    print("value of r",r)
    user = User.objects.all()[r]  
    print("upadted user name", user.uname)
    user.delete();
    return HttpResponse("Record has been Deleted")

def numberOfUser(request):
    user = User.objects.all() 
    print("upadted user name", user)
    a=5
    return HttpResponse(a) 

