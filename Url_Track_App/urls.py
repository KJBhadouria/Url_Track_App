from django.contrib import admin
from django.urls import path
from django.urls.conf import include
#from Superuser_code.admin import super_user
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('Superuser_code.urls')),

    #path('admin/', admin.site.urls),
    #path('', admin.site.urls), # for accesssing admin from blank url
    #path('',super_user.urls),
]

#admin.site.index_title = "TRACK URL"
#admin.site.site_header = "DATA"
#admin.site.site_title = "WELCOME"

