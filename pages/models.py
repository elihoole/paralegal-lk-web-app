from django.db import models


# Create your models here.
class Case(models.Model):
    id = models.AutoField(primary_key=True)
    casenumber = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=100, default="")
    nameofparties = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")

    def __unicode__(self):
        return self.casenumber
