from django.contrib import admin
from . import models

# Register your models here.
class Superusercode(admin.AdminSite):

    site_header= "URL TRACK"

super_user= Superusercode(name="Portalsuperuser")

super_user.register(models.UrlData)  #Registering the model we made to this admin by using super_user
super_user.register(models.Status)  #Registering the model we made to this admin by using super_user
#admin.site.register(models.Status)  #For Registering model to admin, main admin
