from django.urls import path
from .views import HomePageView, AboutPageView, CaseListView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("supreme_court_cases/", CaseListView.as_view(), name="supreme_court_cases"),
]
