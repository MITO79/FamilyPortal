from django.db import models

# 未migrate！！
# Create your models here.
class ta_menu(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=255,default='')
    category_id = models.ForeignKey(ma_category,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ':' + self.menu

class ma_category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255,default='')

    def __str__(self):
        return str(self.id) + ':' + self.category