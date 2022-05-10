from django.db import models

# 未migrate！！
# Create your models here.
class ma_category(models.Model):
    category = models.CharField(max_length=255,default='',unique=True)

    def __str__(self):
        return self.category

class ta_menu(models.Model):
    menu = models.CharField(max_length=255,default='')
    category = models.ForeignKey(ma_category,on_delete=models.PROTECT)
    url = models.URLField(null=False)

    def __str__(self):
        return self.menu

class ta_recipe(models.Model):
    menu = models.ForeignKey(ta_menu)
    ingredient = models.CharField(max_length=255,default='')    #材料
    unit = models.CharField(max_length=255,default='大さじ')
    volume = models.IntegerField(default=0)

    def __str__(self):
        return self.menu


