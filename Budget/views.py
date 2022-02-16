from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class mainviews(TemplateView):
    def __init__(self):
        self.params = {
            'uid':0,
        }

    def get(self,request,uid):
        self.params['uid'] = uid
        return render(request,'Budget/main.html/',context=self.params)

    def post(self,request):
        print('request method is POST')
        return render(request,'Budget/main.html/',context=self.params)