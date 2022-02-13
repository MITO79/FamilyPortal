from django.urls import path
from .views import mainviews,signupviews,loginviews

urlpatterns = [
    path('signup/',signupviews.as_view(),name='signup'),
    path('login/',loginviews.as_view(),name='login'),
    path('',mainviews.as_view(),name='main'),
]