from django.db import models


# Create your models here.
class Judgement(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="")
    nameofparties = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    standard_casenumber = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.standard_casenumber[:20]



