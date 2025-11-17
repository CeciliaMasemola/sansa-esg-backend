from django.urls import path
from . import views

urlpatterns = [
    path("", views.sansa_esg_dashboard, name="dashboard"),
]
