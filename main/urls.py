from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    #path("register/", views.RegisterView.as_view(), name="register"),
]