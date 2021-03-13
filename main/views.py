from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "main/home.html"

