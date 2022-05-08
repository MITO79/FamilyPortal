from django.urls import path
from . import views

urlpatterns = [
    path('<int:uid>/',views.mainviews.as_view(),name='recipe'),
]