from django.urls import path
from adminapp import views


urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('categoryPage/',views.categoryPage,name="categoryPage"),
    path('addCategory/',views.addCategory,name="addCategory"),
    path('Showcategory/',views.Showcategory,name="Showcategory"),
    path('editCategoryPage/',views.editCategoryPage,name="editCategoryPage"),
    path('editCategoryPage/<int:dataid>',views.editCategoryPage,name="editCategoryPage"),
    path('editCategoryData/<int:dataid>',views.editCategoryData,name="editCategoryData"),
    path('deleteCategoryData/<int:dataid>',views.deleteCategoryData,name="deleteCategoryData"),

    path('addClientPage/',views.addClientPage,name="addClientPage"),
    path('addClients/',views.addClients,name="addClients"),
    path('ShowClients/',views.ShowClients,name="ShowClients"),
    path('editClientsPage/<int:dataid>',views.editClientsPage,name="editClientsPage"),
    path('editClientsdata/<int:dataid>',views.editClientsdata,name="editClientsdata"),
    path('deleteClientsData/<int:dataid>',views.deleteClientsData,name="deleteClientsData"),

    path('addPhotosPage/',views.addPhotosPage,name="addPhotosPage"),
    path('addPhotos/',views.addPhotos,name="addPhotos"),
    path('showPhotos/',views.showPhotos,name="showPhotos"),
    path('editPhotosPage/<int:dataid>',views.editPhotosPage,name="editPhotosPage"),
    path('editClientdata/<int:dataid>',views.editClientdata,name="editClientdata"),
    path('deleteImageData/<int:dataid>',views.deleteImageData,name="deleteImageData"),

    path('loginpage/',views.loginpage,name="loginpage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('addPackagePage/',views.addPackagePage,name="addPackagePage"),
    path('addPackkage/',views.addPackkage,name="addPackkage"),
    path('showBookedPage/',views.showBookedPage,name="showBookedPage"),
    path('deletebookedData/<int:dataid>',views.deletebookedData,name="deletebookedData"),
    
    path('showcontactPage/',views.showcontactPage,name="showcontactPage"),
    path('deletecontactData/<int:dataid>',views.deletecontactData,name="deletecontactData"),



]