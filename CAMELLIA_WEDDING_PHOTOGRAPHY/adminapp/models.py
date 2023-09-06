from django.db import models

# Create your models here.
class categoryDB(models.Model):
    CategoryName=models.CharField(max_length=100,null=True,blank=True)
    CategoryImage=models.ImageField(upload_to="Category_Image",null=True,blank=True)

class ClientDB(models.Model):
    ClientName = models.CharField(max_length=100,null=True,blank=True)
    ClientEventCategory = models.CharField(max_length=100,null=True,blank=True)

class ImagesDB(models.Model):
    IMGCategoryName=models.CharField(max_length=100,null=True,blank=True)
    IMGClientName = models.CharField(max_length=100,null=True,blank=True)
    Images=models.ImageField(upload_to="Event-Images",null=True,blank=True)

class CoverImages(models.Model):
    CoverCategoryName=models.CharField(max_length=100,null=True,blank=True)
    CoverCategoryIamges=models.ImageField(upload_to="Cover-Category_Image",null=True,blank=True)

class WeddingPackageDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

class usersignupDB(models.Model):
    userName = models.CharField(max_length=100,null=True,blank=True)
    userEmail = models.EmailField(max_length=100,null=True,blank=True)
    userMobile = models.IntegerField(null=True,blank=True)
    userPassword = models.CharField(max_length=100,null=True,blank=True)
    userImage = models.ImageField(upload_to="userProfile",null=True,blank=True)

class bookinDB(models.Model):
    Package_Name=models.CharField(max_length=100,null=True,blank=True)
    Package_Price = models.IntegerField(null=True,blank=True)
    Name= models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Mobile = models.FloatField(null=True,blank=True)
    Date=models.DateField(null=True,blank=True)

class ContactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
    



