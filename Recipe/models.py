from django.db import models

# 未migrate！！
# Create your models here.
class ta_menu(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=255,default='')
    category_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ':' + self.title

