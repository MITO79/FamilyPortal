from django.urls import path
from .views import mainviews

urlpatterns = [
    path('<int:uid>/',mainviews.as_view(),name='list'),
]