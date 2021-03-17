from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("people/",views.PeopleView.as_view(),name="people"),
        path('ppl/<str:slug>/',views.PersonView.as_view(), name="ppl"),
    #path("register/", views.RegisterView.as_view(), name="register"),
    
]