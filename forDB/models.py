# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendar(models.Model):
    listing_id = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    available = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


class Allcolor(models.Model):
    string_field_0 = models.CharField(max_length=50, blank=True, null=True)
    string_field_1 = models.CharField(max_length=50, blank=True, null=True)
    string_field_2 = models.CharField(max_length=50, blank=True, null=True)
    string_field_3 = models.CharField(max_length=50, blank=True, null=True)
    string_field_4 = models.CharField(max_length=50, blank=True, null=True)
    string_field_5 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allcolor'

class InventoryCt(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


    class Meta:
        managed = False
        db_table = 'inventory_ct'



class Ord1(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord1'

