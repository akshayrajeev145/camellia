from django.shortcuts import render,redirect
from adminapp.models import *
from django.contrib import messages


# Create your views here.
def Mainpage(req):
    return render(req,"mainPage.html")
def aboutpage(req):
    return render(req,"about.html")
def projectpage(req):
    data=categoryDB.objects.all()
    return render(req,"projects.html",{'data':data})
def projectDetailspage(req,cateName):
    imagesdata=ImagesDB.objects.filter(IMGCategoryName=cateName)
    return render(req,"projectDetails.html",{'imagesdata':imagesdata})
def contactPage(req):
    return render(req,"contact.html")

def packagePage(request):
    search_name = request.GET.get('name', '')
    filtered_packages = WeddingPackageDB.objects.filter(name__icontains=search_name)
    context = {
        'filtered_packages': filtered_packages,
        'search_name': search_name,
    }
    return render(request, 'package.html', context)
def bookingPage(req,dataid):
    if 'userName' in req.session:
        username = req.session['userName']
        data = WeddingPackageDB.objects.get(id=dataid)
        return render(req,"bookPage.html",{'data':data,'username': username,})
    else:
        return redirect(bookuserloginpage)


def userloginpage(req):
    return render(req,"userlogin.html")
def userRegData(req):
    if req.method == "POST":
        uname=req.POST.get('uName')
        uemail=req.POST.get('uEmail')
        umobile=req.POST.get('uMobile')
        upassword=req.POST.get('uPassword')
        uimg=req.FILES['uImage']
        obj = usersignupDB(userName=uname,userEmail=uemail,userMobile=umobile,userPassword=upassword,userImage=uimg)
        obj.save()
        return redirect(userloginpage)
def userLogin(req):
    if req.method=="POST":
        uname = req.POST.get('Username')
        pwd = req.POST.get('Password')
        if usersignupDB.objects.filter(userName=uname,userPassword=pwd).exists():
            req.session['userName']=uname
            req.session['userPassword']=pwd
            return redirect(Mainpage)
        else:
            return redirect (userloginpage)
    else:
         return redirect (userloginpage)
def userLogout(req):
    del req.session['userName']
    del req.session['userPassword']
    return redirect(Mainpage)

def bookuserloginpage(req):
    return render(req,"bookuserLogin.html")
def bookuserLogin(req):
    if req.method=="POST":
        uname = req.POST.get('Username')
        pwd = req.POST.get('Password')
        if usersignupDB.objects.filter(userName=uname,userPassword=pwd).exists():
            req.session['userName']=uname
            req.session['userPassword']=pwd
            return redirect(packagePage)
        else:
            return redirect (userloginpage)
    else:
         return redirect (userloginpage)
    
def bookingData(req):
    if req.method == "POST":
        pname=req.POST.get('pack-name')
        pprice=req.POST.get('pack-price')
        cname=req.POST.get('c-name')
        cemail=req.POST.get('c-email')
        cnumber=req.POST.get('c-number')
        date=req.POST.get('c-date')
        obj=bookinDB(Package_Name=pname,Package_Price=pprice,Name=cname,Email=cemail,Mobile=cnumber,Date=date)
        obj.save()
        messages.success(req,"Booked Succesfuly Camelia will Contact You For more information")
        return redirect(Mainpage)  
def contactData(req):
    if req.method == "POST":
        name=req.POST.get('c-name')
        Email=req.POST.get('c-email')
        subject=req.POST.get('c-subject')
        message=req.POST.get('c-message')
        obj=ContactDB(Name=name,Email=Email,Subject=subject,message=message)
        obj.save()
        return redirect(Mainpage)


