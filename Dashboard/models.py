from django.db import models
from django.utils import timezone
# Create your models here.

class ma_table(models.Model):
    id = models.AutoField(primary_key=True)
    table = models.CharField(max_length=64)
    def __str__(self):
        return str(self.id) + ':' + self.table

class ma_status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=64)
    def __str__(self):
        return str(self.id) + ':' + self.status

class ma_listType(models.Model):
    id = models.AutoField(primary_key=True)
    listType = models.CharField(max_length=64)
    def __str__(self):
        return str(self.id) + ':' + self.listType

class ta_log(models.Model):
    id = models.AutoField(primary_key=True)
    uid_id = models.IntegerField(default=0)
    table_id = models.IntegerField(default=0)
    inTable_id = models.IntegerField(default=0)
    status_id = models.IntegerField(default=0)
    updateDay = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.updateDay) + ' table_id = ' + str(self.table_id)
