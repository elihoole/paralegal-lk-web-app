from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count
from .models import Judgement
from django.db.models import Q


from django.shortcuts import render
from .forms import JudgementsFilterForm, JudgementsSearchForm

from . import bm25
import json

# Create your views here.


class HomePageView(TemplateView):
    model = Judgement
    template_name = "home.html"
    context_object_name = "search_judgements_list"

    with open("pos_inv_ind.json", "r") as f:
        data = json.load(f)
        dlt = bm25.createDocTable(data)
        # print("dlt", dlt)

    def get(self, request, *args, **kwargs):
        query = request.GET.get("search_query")
        print("query", query)
        if query:
            results = bm25.search(query, self.data, self.dlt)[:20]
            queryset = Judgement.objects.filter(Q(primary_key__in=results))
            # re order queryset by results
            queryset = sorted(queryset, key=lambda x: results.index(x.primary_key))

        else:
            queryset = Judgement.objects.none()
        return render(
            request,
            "home.html",
            {
                "query": query,
                "results": queryset,
                "search_form": JudgementsSearchForm(),
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = kwargs.get("search_form", JudgementsSearchForm())
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"


class JudgementListView(ListView):
    model = Judgement
    template_name = "judgements_list.html"
    context_object_name = "all_judgements_list"

    def get(self, request, *args, **kwargs):
        year_ = request.GET.get("year")
        month_ = request.GET.get("month")

        month_keys = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
        }

        if year_ and not month_:
            queryset = (
                self.get_queryset()
                .annotate(year=ExtractYear("date"))
                .filter(year=year_)
            )
        elif year_ and month_:
            queryset = (
                self.get_queryset()
                .annotate(year=ExtractYear("date"), month=ExtractMonth("date"))
                .filter(year=year_, month=month_keys[month_])
            )
        else:
            queryset = self.get_queryset()

        self.object_list = queryset
        context = self.get_context_data(
            object_list=queryset,
            filter_form=JudgementsFilterForm(),
            year=year_ if year_ != None else None,
            month=month_ if month_ != None else None,
        )
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = kwargs.get("filter_form", JudgementsFilterForm())
        return context
