from django.shortcuts import render,redirect
from adminapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def homepage(req):
    return render(req,"index.html")
def categoryPage(req):
    data=categoryDB.objects.all()
    return render(req,"addCategory.html",{'data':data})
def addCategory(req):
    if req.method =="POST":
        cname=req.POST.get('c-name')
        cimage=req.FILES['c-image']
        obj=categoryDB(CategoryName=cname,CategoryImage=cimage)
        obj.save()
        return redirect(categoryPage)
def Showcategory(req):
    data=categoryDB.objects.all()
    return render(req,"showCategory.html",{'data':data})
def editCategoryPage(req,dataid):
    data=categoryDB.objects.get(id=dataid)
    return render(req,"editCategoruPage.html",{'data':data})
def editCategoryData(req, dataid):
    if req.method == "POST":
        cname = req.POST.get('c-name')
        try:
            cimg = req.FILES['c-image']
            fs = FileSystemStorage()
            img = fs.save(cimg.name, cimg)
        except MultiValueDictKeyError:
            img = categoryDB.objects.get(id=dataid).CategoryImage
        categoryDB.objects.filter(id=dataid).update(CategoryName=cname, CategoryImage=img)
        return redirect(Showcategory)
def deleteCategoryData(req,dataid):
    data = categoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(Showcategory)

def addClientPage(req):
    data=categoryDB.objects.all()
    return render(req,"addClient.html",{'data':data})
def addClients(req):
    if req.method=="POST":
        cname=req.POST.get("c-name")
        ccategory=req.POST.get("c-category")
        obj=ClientDB(ClientName=cname,ClientEventCategory=ccategory)
        obj.save()
        return redirect(addClientPage)
def ShowClients(req):
    data=ClientDB.objects.all()
    return render(req,"showClients.html",{'data':data})
def editClientsPage(req,dataid):
    data=ClientDB.objects.get(id=dataid)
    cate=categoryDB.objects.all()
    return render(req,"editClientsPage.html",{'cate':cate,'data':data})
def editClientsdata(req,dataid):
    if req.method=="POST":
        cname=req.POST.get("c-name")
        ccategory=req.POST.get("c-category")
        ClientDB.objects.filter(id=dataid).update(ClientName=cname,ClientEventCategory=ccategory)
        return redirect(ShowClients)
def deleteClientsData(req,dataid):
    data = ClientDB.objects.filter(id=dataid)
    data.delete()
    return redirect(ShowClients)

def addPhotosPage(req):
    data=categoryDB.objects.all()
    cli=ClientDB.objects.all()
    return render(req,"addPhotos.html",{'data':data,'cli':cli}) 
def addPhotos(req):
    if req.method == "POST":
        name=req.POST.get("cl-name")
        cate=req.POST.get("cl-category")
        img=req.FILES['cl-image']
        obj=ImagesDB(IMGClientName=name,IMGCategoryName=cate,Images=img)
        obj.save()
        return redirect(addPhotosPage)
def showPhotos(req):
    data=ImagesDB.objects.all()
    return render(req,"showPhotos.html",{'data':data})
def editPhotosPage(req,dataid):
    data=ImagesDB.objects.get(id=dataid)
    cata=categoryDB.objects.all()
    cli=ClientDB.objects.all()
    return render(req,"editPhotosPage.html",{'data':data,'cata':cata,'cli':cli})
def editClientdata(req,dataid):
    if req.method == "POST":
        name=req.POST.get("cl-name")
        cate=req.POST.get("cl-category")
        try:
            img = req.FILES['cl-image']
            fs = FileSystemStorage()
            img = fs.save(img.name, img)
        except MultiValueDictKeyError:
            img = categoryDB.objects.get(id=dataid).CategoryImage
        ImagesDB.objects.filter(id=dataid).update(IMGClientName=name,IMGCategoryName=cate,Images=img)
        return redirect(showPhotos)
def deleteImageData(req,dataid):
    data = ImagesDB.objects.filter(id=dataid)
    data.delete()
    return redirect(showPhotos)
def loginpage(req):
    return render(req,"login.html")

def admin_login(req):
    if req.method=="POST":
        uname=req.POST.get('username')
        pwd=req.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(req,user)
                return redirect(homepage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)            
def admin_logout(req):
    return redirect(loginpage)

def addPackagePage(req):
    return render(req,"addPackage.html")
def addPackkage(req):
    if req.method=='POST':
        pname=req.POST.get('p-name')
        pdes=req.POST.get('p-des')
        pprice=req.POST.get('p-price')
        obj=WeddingPackageDB(name=pname,description=pdes,price=pprice,)
        obj.save()
        return redirect(addPackagePage)
    
def showBookedPage(req):
    data=bookinDB.objects.all()
    return render(req,"showBooked.html",{'data':data})
def deletebookedData(req,dataid):
    data = bookinDB.objects.filter(id=dataid)
    data.delete()
    return redirect(showBookedPage)

def showcontactPage(req):
    data=ContactDB.objects.all()
    return render(req,"showcontact.html",{'data':data})
def deletecontactData(req,dataid):
    data = ContactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(showcontactPage)

    




