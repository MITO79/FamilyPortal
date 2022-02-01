from django.db import models

# Create your models here.
class ta_list(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default='未タイトル')
    content = models.CharField(max_length=255,null=True)
    listType_id = models.IntegerField(default=0)
    flg_1 = models.IntegerField(default=0)
    flg_2 = models.IntegerField(default=0)
    flg_3 = models.IntegerField(default=0)
    flg_4 = models.IntegerField(default=0)
    flg_5 = models.IntegerField(default=0)
    flg_6 = models.IntegerField(default=0)
    flg_7 = models.IntegerField(default=0)
    flg_8 = models.IntegerField(default=0)
    flg_9 = models.IntegerField(default=0)
    flg_10 = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + ':' + self.title

