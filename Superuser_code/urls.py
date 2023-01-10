from django.contrib import admin
from django.urls import path
from django.urls.conf import include
#from Superuser_code.admin import super_user
from . import views

urlpatterns = [

    #path('admin/', admin.site.urls),
    path('',views.test , name="test"),
]


