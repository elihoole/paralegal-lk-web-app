from django.urls import path
from .views import HomePageView, AboutPageView, CaseListView

urlpatterns = [
    path(
        "supreme_court_judgements/",
        CaseListView.as_view(),
        name="supreme_court_judgements",
    ),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
