from django.urls import path
from webapp import views


urlpatterns = [
     path('',views.Mainpage,name="Mainpage"),   
     path('aboutpage/',views.aboutpage,name="aboutpage"),   
     path('contactPage/',views.contactPage,name="contactPage"),   
     path('projectpage/',views.projectpage,name="projectpage"),   
     path('projectDetailspage/<cateName>',views.projectDetailspage,name="projectDetailspage"),   
     path('packagePage/',views.packagePage,name="packagePage"), 
     path('bookingPage/<int:dataid>',views.bookingPage,name="bookingPage"),

     path('userloginpage/',views.userloginpage,name="userloginpage"),
     path('userRegData/',views.userRegData,name="userRegData"),
     path('userLogin/',views.userLogin,name="userLogin"),
     path('userLogout/',views.userLogout,name="userLogout"),

     path('bookuserloginpage/',views.bookuserloginpage,name="bookuserloginpage"),
     path('bookuserLogin/',views.bookuserLogin,name="bookuserLogin"),
     path('bookingData/',views.bookingData,name="bookingData"),
     path('contactData/',views.contactData,name="contactData"),
  
]