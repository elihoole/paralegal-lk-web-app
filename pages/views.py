from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count
from .models import Judgement

from django.shortcuts import render
from .forms import JudgementsFilterForm


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class JudgementListView(ListView):
    model = Judgement
    template_name = "judgements_list.html"
    context_object_name = "all_judgements_list"

    def get(self, request, *args, **kwargs):
        year = request.GET.get("year")
        month = request.GET.get("month")

        if year and month:
            queryset = (
                self.get_queryset()
                .annotate(year=ExtractYear("date"), month=ExtractMonth("date"))
                .filter(year=year, month=month)
            )
        else:
            queryset = self.get_queryset()

        month_names = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        self.object_list = queryset
        context = self.get_context_data(
            object_list=queryset,
            filter_form=JudgementsFilterForm(),
            year=year if year != None else None,
            month=month_names[int(month)] if month != None else None,
        )
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = kwargs.get("filter_form", JudgementsFilterForm())
        return context


def search_form(request):
    return render(request, "search_form.html")


def judgements_search(request):
    form = JudgementsFilterForm(request.GET)

    if form.is_valid():
        year = form.cleaned_data["year"]
        month = form.cleaned_data["month"]
        judgements = Judgement.objects.filter(date__year=year, date__month=month)

    else:
        judgements = Judgement.objects.all()
    return render(
        request, "judgements_search.html", {"form": form, "judgements": judgements}
    )
