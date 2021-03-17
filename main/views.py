from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from .models import Book, Influencer

class HomePageView(TemplateView):
    template_name = "main/home.html"

class PeopleView(View):

    def get(self, request, *args, **kwargs):
        influencers = [item for item in Influencer.objects.all()]   
        return render(request,'main/people.html',{'people': influencers})
        

class PersonView(View):
    def get(self, request, *args, **kwargs):
        slug= kwargs.get('slug')
        influencer = Influencer.objects.filter(slug=slug).first()
        if influencer is None:
            return(redirect('/'))
        else:
            return render(request,'main/person.html',{'influencer':influencer})
    