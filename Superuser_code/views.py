from django.shortcuts import render
from django.http import HttpResponse
from .tasks import apihit

# Create your views here.
def test(request):
    print("Hello jaya")
    apihit.delay()
    #apihit.apply_async( queue = 'low_priority' , args = ())
    #apihit()
    return HttpResponse("Done")

