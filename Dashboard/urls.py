from django.urls import path
from .views import mainviews

urlpatterns = [
    path('',mainviews.as_view(),name='dashboard'),
]