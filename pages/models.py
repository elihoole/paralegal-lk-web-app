from django.db import models
from django import forms


# Create your models here.
class Judgement(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="")
    nameofparties = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    standard_casenumber = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.standard_casenumber[:20]


class JudgmentsFilterForm(forms.Form):
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2009, 2024)]
    MONTH_CHOICES = [(str(month), str(month)) for month in range(1, 13)]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    month = forms.ChoiceField(choices=MONTH_CHOICES)
