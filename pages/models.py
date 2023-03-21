from django.db import models
from . import bm25
import re
import string


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

    def get_relevant_text_main_func(self, query):
        """
        get 100 characters before and after most relevant word in query with regex
        """

        if query.find("&") != -1:
            queries = query.split("&")
            queries = [bm25.clean_up_case_text(q).strip() for q in queries]

            sub_query_rel_text = {}
            for sub_query in queries:
                sub_query_rel_text[sub_query] = self.get_relevant_text_from_query(
                    sub_query
                )

            # return by concatenating the values
            return " ".join(sub_query_rel_text.values())
        else:
            return self.get_relevant_text_from_query(query)

    def get_relevant_text_from_query(self, query):
        query = bm25.clean_up_case_text(query)

        # remove punctuation from query

        # use regex to get 100 characters before and after most relevant word in query
        pattern = r"[\.\?!\n].+\s+" + query.strip() + r"\s+.+[\.\?!\n]"

        matches = re.findall(pattern, self.judgement_text.lower())

        # get the start and end index of matches[0] in self.judgement_text

        if matches:
            sentence = matches[0]
            start = self.judgement_text.lower().find(sentence)
            end = start + len(sentence)
            return self.judgement_text[start:end]
        else:
            query = query.split(" ")[0]
            # use regex to get 100 characters before and after most relevant word in query
            pattern = r"[\.\?!\n].+\s+" + query.strip() + r"\s+.+[\.\?!\n]"
            matches = re.findall(pattern, self.judgement_text.lower())
            if matches:
                sentence = matches[0]
                start = self.judgement_text.lower().find(sentence)
                end = start + len(sentence)
                return self.judgement_text[start:end]
            else:
                return ""
