#models
from django.db import models

class Calendar(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'

#class Allcolor(models.Model):
#    string_field_0 = models.CharField(max_length=255)
#    string_field_1 = models.ForeignKey('InventoryCt', on_delete=models.CASCADE, related_name='allcolors', db_column='string_field_1')
#    string_field_2 = models.CharField(max_length=255)
#    string_field_3 = models.CharField(max_length=255)
#    string_field_4 = models.CharField(max_length=255)
#    string_field_5 = models.CharField(max_length=255)
#    class Meta:
#        managed = False
#        db_table = 'allcolor'


class Allcolor(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    color_code = models.CharField(max_length=50, blank=True, null=True)
    ct1 = models.CharField(max_length=50, blank=True, null=True)
    ct2 = models.CharField(max_length=50, blank=True, null=True)
    ct3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allcolor'




class InventoryCt(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', max_length=255, primary_key=True)
    on_hand = models.IntegerField(db_column='On Hand')

    class Meta:
        managed = False
        db_table = 'inventory_ct'


class Ord1(models.Model):
    item = models.CharField(max_length=255, primary_key=True)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord1'

class CtAc(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item = models.CharField(max_length=50, blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    color_code = models.CharField(max_length=50, blank=True, null=True)
    ct1 = models.CharField(max_length=50, blank=True, null=True)
    ct2 = models.CharField(max_length=50, blank=True, null=True)
    ct3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_ac'

class Ord2Ac(models.Model):
    item = models.CharField(max_length=50, primary_key=True)  # primary_key=True 옵션 추가
    pcs = models.IntegerField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    # 다른 필드들...

    class Meta:
        managed = False
        db_table = 'ord2_ac'

class Ord3Ac(models.Model):
    item = models.CharField(max_length=50, primary_key=True)  # primary_key=True 옵션 추가
    pcs = models.IntegerField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    # 다른 필드들...

    class Meta:
        managed = False
        db_table = 'ord3_ac'



class CtRoomStatus(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj4_2 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa1_7 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    on_hand = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_room_status'


class CtRoomStatus_r1(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj4_2 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa1_7 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    on_hand = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    on_hand_diff = models.FloatField(blank=True, null=True)  # NY - On Hand

    def save(self, *args, **kwargs):
        self.on_hand_diff = self.ny - self.on_hand if self.ny and self.on_hand else None
        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'ct_room_status_r1'


class Po300(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po300'

class Po301(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po301'

