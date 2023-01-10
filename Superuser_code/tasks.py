from celery import shared_task
import urllib.request

@shared_task(bind = True)
def apihit(self):
    '''print("inside func")
    for i in range(10):
        print(i)'''

    
    x = urllib.request.urlopen("https://www.youtube.com/").getcode()
    if x<400 :
        print ("Inside function Pass",x)
    else:
        print("Inside function Fail")

    text=open("logs.txt","a")
    text.write("Result of log : " + str(x))
    text.write("\n")
    text.close()


    return "Done"

    