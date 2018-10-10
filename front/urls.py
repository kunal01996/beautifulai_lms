# front/urls.py
from django.urls import path
from .views import HomePageView, AboutUsPageView

urlpatterns = [
    path('about/', AboutUsPageView.as_view(), name="about"),
    path('', HomePageView.as_view(), name='home'),
]