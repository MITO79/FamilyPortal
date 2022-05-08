from django import forms
from . import models

pass
# # アンケート用フォーム
# class EnquetteForm(forms.ModelForm):
    
#     listType_id = forms.IntegerField(initial=3,label='リストタイプ')
#     title = forms.ChoiceField(
#         label='何を聞きたい？',
#         choices=[
#             ('今日の夕飯は？','今日の夕飯は？'),
#             ('週末何する？','週末何する？'),
#             ('どちらがいい？','どちらがいい？'),
#             ('その他','その他'),
#         ]
#     )

#     class Meta():
#         model = models.ta_list
#         fields = (
#             'title',
#             'content',
#             'listType_id',
#             'sub_1',
#             'sub_2',
#             'sub_3',
#             'sub_4',
#             'sub_5',
#             'sub_6',
#             'sub_7',
#             'sub_8',
#             'sub_9',
#             'sub_10',
#             'flg_1',
#             'flg_2',
#             'flg_3',
#             'flg_4',
#             'flg_5',
#             'flg_6',
#             'flg_7',
#             'flg_8',
#             'flg_9',
#             'flg_10',
#         )
        
#         labels = {
#             # 'title':'何を聞きたい？',
#             'content':'聞きたいこと',
#             # 'listType_id':'リストタイプ',
#             'sub_1':'1.',
#             'sub_2':'2.',
#             'sub_3':'3.',
#             'sub_4':'4.',
#             'sub_5':'5.',
#             'sub_6':'6.',
#             'sub_7':'7.',
#             'sub_8':'8.',
#             'sub_9':'9.',
#             'sub_10':'10.',
#             'flg_1':'1.',
#             'flg_2':'2.',
#             'flg_3':'3.',
#             'flg_4':'4.',
#             'flg_5':'5.',
#             'flg_6':'6.',
#             'flg_7':'7.',
#             'flg_8':'8.',
#             'flg_9':'9.',
#             'flg_10':'10.',
#         }
