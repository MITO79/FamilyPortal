from tkinter import CASCADE
from django.db import models

# 未migrate！！
# Create your models here.
class ma_category(models.Model):
    category = models.CharField(max_length=255,default='',unique=True)
    def __str__(self):
        return self.category

class ma_rank(models.Model):
    rank = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.rank

class ta_menu(models.Model):
    menu = models.CharField(max_length=255,default='')
    category = models.ForeignKey(ma_category,on_delete=models.SET_DEFAULT,default=1)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.menu

class ta_request(models.Model):
    menu = models.ForeignKey(ta_menu,on_delete=models.CASCADE)
    rank = models.ForeignKey(ma_rank,on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return self.menu