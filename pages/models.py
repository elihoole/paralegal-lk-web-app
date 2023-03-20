from django.db import models
from . import bm25
import re


# Create your models here.
class Judgement(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    standard_casenumber = models.CharField(max_length=100, default="")
    standard_nameofparties = models.CharField(max_length=100, default="")
    in_the_matter_of = models.CharField(max_length=100, default="")
    primary_key = models.CharField(max_length=100, default="Unavailable")
    judgement_text = models.TextField()

    def __str__(self):
        return self.standard_casenumber[:20]

    def get_relevant_text(self, query):
        """
        get 100 characters before and after most relevant word in query with regex
        """
        query = bm25.clean_up_case_text(query)

        # use regex to get 100 characters before and after most relevant word in query
        pattern = r"(.{0,100}" + query.strip() + r".{0,100})"

        matches = re.findall(pattern, self.judgement_text.lower(), re.MULTILINE)

        # get the start and end index of matches[0] in self.judgement_text

        if matches:
            start = self.judgement_text.lower().find(matches[0])
            end = start + len(matches[0])
            return self.judgement_text[start:end]
        else:
            return ""
