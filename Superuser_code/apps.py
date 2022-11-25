from django.apps import AppConfig
#from django.contrib.admin.apps import AdminConfig

#superadminconfig is to change default admin site from default to superadminconfig
'''class superadminconfig(AdminConfig):
    #default_site = 'Superuser_code.admin.Superusercode'
    name ="Super user"'''

class SuperuserCodeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Superuser_code'
