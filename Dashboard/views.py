from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class mainviews(TemplateView):
    def __init__(self):
        self.params = {
            'uid':0,
        }

    def get(self,request):
        print('request method is GET')
        return render(request,'Dashboard/main.html/',context=self.params)
    
    def post(self,request):
        print('request method is POST')
        return render(request,'Dashboard/main.html/',context=self.params)