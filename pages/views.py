from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Case


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class CaseListView(ListView):
    model = Case
    template_name = "caselist.html"
    context_object_name = "all_cases_list"
