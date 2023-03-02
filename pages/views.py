from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Case


# Create your views here.


class HomePageView(ListView):
    model = Case
    template_name = "home.html"
    context_object_name = "all_cases_list"


class AboutPageView(TemplateView):
    template_name = "about.html"
