#schtasks /create /tn "Security Script" /tr sec.vbs /sc minute /mo 1 /st 19:25 /et 19:30 /k

from apscheduler.schedulers.background import BackgroundScheduler
import time
import urllib.request
from . import models #UrlData


#urlsd=models.UrlData.objects.all()
#context= {
#    'urlsd' : urlsd
#}
#print(context)
{{all}}


def apihit(sometext):
    for item in all :
        hit_url=item.url_name

        #x = urllib.request.urlopen("https://www.youtube.com/").getcode()
        x = urllib.request.urlopen(hit_url).getcode()
        if x<400 :
            print ("Inside function Pass",x)
            print(hit_url)
        else:
            print("Inside function Fail")
            print(hit_url)
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

