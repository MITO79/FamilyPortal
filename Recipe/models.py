from django.db import models

# 未migrate！！
# Create your models here.
class ma_category(models.Model):
    category = models.CharField(max_length=255,default='',unique=True)

    def __str__(self):
        return self.category

class ta_menu(models.Model):
    menu = models.CharField(max_length=255,default='')
    category = models.ForeignKey(ma_category,on_delete=models.SET_DEFAULT,default=0)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.menu