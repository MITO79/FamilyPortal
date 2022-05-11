from django import forms
from . import models

# アンケート用フォーム
class MenuForm(forms.ModelForm):
    
    class Meta():
        model = models.ta_menu
        fields = (
            'menu',
            'category',
            'url',
        )
        
        labels = {
            'menu':'メニュー',
            'category':'カテゴリー',
            'url':'URL',
        }
