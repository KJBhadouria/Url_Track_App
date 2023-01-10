from django.contrib import admin
from . import models
from apscheduler.schedulers.background import BackgroundScheduler
import time
import urllib.request
import threading
import time

# Register your models here.
class Superusercode(admin.AdminSite):

    site_header= "URL TRACK"

super_user= Superusercode(name="Portalsuperuser")

super_user.register(models.UrlData)  #Registering the model we made to this admin by using super_user
super_user.register(models.Status)  #Registering the model we made to this admin by using super_user
#admin.site.register(models.Status)  #For Registering model to admin, main admin

class UrlDataAdmin(admin.ModelAdmin):
    list_display = ['uid', 'url_name','status','up_since','frequency','frequency_Interval']


'''urlsd=models.UrlData.objects.all()
context= {
    'urlsd' : urlsd
}
print(context)


def apihit(sometext):
    x = urllib.request.urlopen("https://www.youtube.com/").getcode()
    if x<400 :
        print ("Inside function Pass",x)
    else:
        print("Inside function Fail")
    return x
    

sched = BackgroundScheduler(timezone= "Asia/Kolkata")
sched.start()
#text = "I am proud of you /n"
x=200
job = sched.add_job(apihit,'cron',[x],second='*/5')
#job = sched.add_job(print,'cron',text,second='*/5')
print(job)

while True:
    time.sleep(5)
    text=open("logs.txt","a")
    text.write(str(job))
    text.write("\n")
    text.close()
    print ("Hello")
    print(job)
'''