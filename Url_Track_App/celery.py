from __future__ import absolute_import, unicode_literals
import os
from celery import Celery  
from django.conf import settings
from celery.schedules import crontab  

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Url_Track_App.settings')
app = Celery('Url_Track_App')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings , namespace= 'CELERY')

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'RRequest : {self.request!r}')
    print("jya")



#WE WILL ADD CELERY SETTINGS HERE
#print("jya")
###############

#Celery Beat Settings  
#app.conf.schedule_beat = {  
#        'every-15-seconds': {
#        'task': 'tasks.add',
#        'schedule': 15.0,
#        'args': (16, 16)
#  
#    }  
#      
#}  
  

