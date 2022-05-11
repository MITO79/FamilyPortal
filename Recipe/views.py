from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from . import models

# Create your views here.
class mainviews(TemplateView):
    def __init__(self):
        self.params = {
            'uid':0,
            'request':models.ta_request(),
        }

    def get(self,request,uid):
        self.params['uid'] = uid
        return render(request,'Recipe/main.html/',context=self.params)

    def post(self,request):
        print('request method is POST')
        return render(request,'Recipe/main.html/',context=self.params)