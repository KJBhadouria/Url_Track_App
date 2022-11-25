from django.contrib import admin
from django.urls import path
from Superuser_code.admin import super_user

urlpatterns = [

    path('admin/', admin.site.urls),

    #path('admin/', admin.site.urls),
    #path('', admin.site.urls), # for accesssing admin from blank url
    path('',super_user.urls),
]

#admin.site.index_title = "TRACK URL"
#admin.site.site_header = "DATA"
#admin.site.site_title = "WELCOME"

