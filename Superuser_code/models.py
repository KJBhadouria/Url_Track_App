from django.db import models

# Create your models here.
#class urls(models.Model):
#    sid = models.IntegerField()


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class UrlData(models.Model):
    uid         = models.AutoField(primary_key=True)
    url_name    = models.CharField(max_length=500)
    status      = models.ForeignKey(Status, on_delete=models.PROTECT, default=1)
    up_since    = models.DateTimeField()
    frequency   = models.IntegerField()
    frequency_Interval  = models.IntegerField()

    class Meta:
        verbose_name = ("Url Data")
        verbose_name_plural = ("Urls Data")
        #ordering =('-publish',)
    
    def __str__(self):
        return self.url_name

