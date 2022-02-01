from django.db import models
import datetime

# Create your models here.
class ta_schedule(models.Model):
    dt = datetime.datetime.today()

    id = models.AutoField(primary_key=True)
    uid_id = models.AutoField(default=0)
    targetDay = models.DateField(default=dt.date())
    content = models.CharField(max_length=255,null=True)
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
        return str(self.id) + ':' + self.targetDay
