from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from .models import Book, Influencer

class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        filtered_list = ['Elon Musk','Bill Gates', 'Barack Obama']
        featured_people = Influencer.objects.filter(name__in=filtered_list)
        context = {"featured_influencers":featured_people}
        return render(request, 'main/home.html', context=context)


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
    