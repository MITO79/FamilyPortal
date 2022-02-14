from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UidForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
class mainviews(TemplateView):
    def __init__(self):
        self.params = {
            'check_uid':False,
            'uid_form':UidForm(),
        }

    def get(self,request):
        self.params['uid_form'] = UidForm()
        self.params['check_uid'] = False
        return render(request,'Login/main.html',context=self.params)

    def post(self,request):
        #POSTの内容をFormに当てはめる
        self.params['uid_form']  = UidForm(request.POST)
        
        #当てはめがうまくいったときの処理
        if self.params['uid_form'].is_valid():
            self.username = self.params['uid_form']['username'].value()
            self.password = self.params['uid_form']['password'].value()
            self.first_name =  self.params['uid_form']['first_name'].value()
            self.judge = authenticate(username=self.username,password=self.password)
            print(self.judge)
        #     print(self.username)
        #     print(self.password)
        #     print(self.first_name)
        #     self.obj = User.objects.filter(username=self.username)

        
        self.params['uid_form'] = UidForm()
        return render(request,'Login/main.html',context=self.params)

class signupviews(TemplateView):
    def __init__(self):
        self.params = {
            'check_uid':False,
            'uid_form':UidForm(),
        }

    # get処理　クラスベースビューでのgetの取り扱いは必ずこの関数名にすること
    def get(self,request):
        self.params['uid_form'] = UidForm()
        self.params['check_uid'] = False
        return render(request,'Login/signup.html',context=self.params)

    def post(self,request):
        self.params['uid_form'] = UidForm(data=request.POST)
        if self.params['uid_form'].is_valid():
            self.params['uid_fo']
            # #フォームの内容をDBに登録
            # account = self.params['uid_form'].save()
            # #パスワードをハッシュ化
            # account.set_password(account.password)
            # #パスワードを更新
            # account.save()

        else:
            print(self.params['uid_form'].errors)
        
        return render(request,'Login/signup.html',context=self.params)


class loginviews(TemplateView):
    pass