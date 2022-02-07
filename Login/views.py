from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UidForm

# Create your views here.
class mainviews():
    pass

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
            #フォームの内容をDBに登録
            account = self.params['uid_form'].save()
            #パスワードをハッシュ化
            account.set_password(account.password)
            #パスワードを更新
            account.save()

        else:
            print(self.params['uid_form'].errors)
        
        return render(request,'Login/signup.html',context=self.params)


class loginviews():
    pass