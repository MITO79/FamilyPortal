from django.urls import path
from .views import mainviews,signupviews

urlpatterns = [
    path('signup/',signupviews.as_view(),name='signup'),
    path('',mainviews.as_view(),name='main'),
]