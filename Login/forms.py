from attr import fields
from django import forms
from django.contrib.auth.models import User

class UidForm(forms.ModelForm):
    # パスワード非表示
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド
        fields = (
            'username',
            'email',
            'password',
            'last_name',
            'first_name',
            )
        # フィールド名
        labels = {
            'username':"名前",
            'email':"メールアドレス",
            'last_name':"苗字",
            'first_name':"家族のあいことば",
            }