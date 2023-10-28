#models
from django.db import models





class Calendar(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


class Allcolor(models.Model):
    string_field_0 = models.CharField(max_length=255)
    string_field_1 = models.CharField(max_length=255, primary_key=True)
    string_field_2 = models.CharField(max_length=255)
    string_field_3 = models.CharField(max_length=255)
    string_field_4 = models.CharField(max_length=255)
    string_field_5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'allcolor'

class InventoryCt(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', max_length=255, primary_key=True)  # changed line
    on_hand = models.IntegerField(db_column='On Hand')  # 변경된 줄



    class Meta:
        managed = False
        db_table = 'inventory_ct'


class Ord1(models.Model):
    item = models.CharField(max_length=255, primary_key=True)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord1'
