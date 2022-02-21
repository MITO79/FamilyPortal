from django.db import models

# Create your models here.
class ta_list(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default='未タイトル')
    content = models.CharField(max_length=255,default='')
    listType_id = models.IntegerField(default=0)
    sub_1 = models.CharField(max_length=255,default='')
    sub_2 = models.CharField(max_length=255,default='')
    sub_3 = models.CharField(max_length=255,default='')
    sub_4 = models.CharField(max_length=255,default='')
    sub_5 = models.CharField(max_length=255,default='')
    sub_6 = models.CharField(max_length=255,default='')
    sub_7 = models.CharField(max_length=255,default='')
    sub_8 = models.CharField(max_length=255,default='')
    sub_9 = models.CharField(max_length=255,default='')
    sub_10 = models.CharField(max_length=255,default='')
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
    date_1 = models.DateTimeField(null=True)
    date_2 = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id) + ':' + self.title

