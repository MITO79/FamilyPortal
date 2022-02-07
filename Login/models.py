from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ta_uid(models.Model):
    # User機能でユーザー名、パスワード、メールアドレスをまとめて生成できる
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # 追加要素
    #id = models.AutoField()
    
    def __str__(self):
        return str(self.id) + ':' + self.user.username