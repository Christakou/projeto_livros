from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml')),
    path("", views.HomePageView.as_view(), name="homepage"),
    path("pessoas/",views.PeopleView.as_view(),name="people"),
        path('livros-recomendados-por-<str:slug>/',views.PersonView.as_view(), name="ppl"),
    #path("register/", views.RegisterView.as_view(), name="register"),
    
]