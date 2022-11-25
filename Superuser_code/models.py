from django.db import models

# Create your models here.
#class urls(models.Model):
#    sid = models.IntegerField()

    
class UrlData(models.Model):
    uid         = models.AutoField(primary_key=True)
    url_name    = models.CharField(max_length=500)
    status      = models.CharField(max_length=7)
    up_since    = models.DateTimeField()
    frequency   = models.IntegerField()
    frequency_Interval  = models.IntegerField()
    
    def __str__(self):
        return self.url_name