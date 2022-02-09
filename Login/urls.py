from django.urls import path
from .views import mainviews,signupviews,loginviews

urlpatterns = [
    path('',mainviews,name='main'),
    path('signup/',signupviews.as_view(),name='signup'),
    path('login/',loginviews,name='login'),
]