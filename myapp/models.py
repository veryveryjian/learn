
from django.db import models




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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calendar(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


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


class Cw2OrderData(models.Model):
    id = models.IntegerField(primary_key=True)
    avgg = models.FloatField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    o305 = models.IntegerField(blank=True, null=True)
    o306 = models.IntegerField(blank=True, null=True)
    o307 = models.IntegerField(blank=True, null=True)
    o308 = models.IntegerField(blank=True, null=True)
    o309 = models.IntegerField(blank=True, null=True)
    o342 = models.IntegerField(blank=True, null=True)
    o344 = models.IntegerField(blank=True, null=True)
    o346 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw2_order_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InventoryCt(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.CharField(db_column='Reorder Pt (Min)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.CharField(max_length=50, blank=True, null=True)
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.FloatField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.FloatField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.FloatField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.FloatField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.FloatField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.FloatField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory_ct'


class InventoryMiller(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.CharField(db_column='Reorder Pt (Min)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.CharField(max_length=50, blank=True, null=True)
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.FloatField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.FloatField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.FloatField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.FloatField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.FloatField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.FloatField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory_miller'


class InventoryNj(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.FloatField(db_column='Reorder Pt (Min)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.FloatField(blank=True, null=True)
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.FloatField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.FloatField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.FloatField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.FloatField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.FloatField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.FloatField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory_nj'


class InventoryNy(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.CharField(db_column='Reorder Pt (Min)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.CharField(max_length=50, blank=True, null=True)
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.FloatField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.FloatField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.FloatField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.FloatField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.FloatField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.FloatField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory_ny'


class InventoryPa(models.Model):
    unnamed_0 = models.CharField(db_column='Unnamed: 0', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.CharField(db_column='Reorder Pt (Min)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.CharField(max_length=50, blank=True, null=True)
    on_hand = models.FloatField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.FloatField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.FloatField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.FloatField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.FloatField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.FloatField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.FloatField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory_pa'


class Ord2(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord2'


class Ord2Ac(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    color_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord2_ac'


class Ord3(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord3'


class Ord3Ac(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    color_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord3_ac'


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


class RoomCw2(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj13 = models.IntegerField(blank=True, null=True)
    pa7 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_cw2'


class RoomE2(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj9 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa5 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_e2'


class RoomMs(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj4_2 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa1_7 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'room_ms'


class RoomSe(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj6_5 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa4_2 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_se'


class RoomSg(models.Model):
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj3_5 = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa3_5 = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_sg'


class RoomStatus(models.Model):
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
        db_table = 'room_status'


class Test1(models.Model):
    column1 = models.CharField(max_length=50, blank=True, null=True)
    item_description = models.CharField(db_column='Item Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_pt_min_field = models.CharField(db_column='Reorder Pt (Min)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max = models.CharField(max_length=50, blank=True, null=True)
    on_hand = models.IntegerField(db_column='On Hand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    on_sales_order = models.IntegerField(db_column='On Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    for_assemblies = models.IntegerField(db_column='For Assemblies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.IntegerField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.IntegerField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.IntegerField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.IntegerField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item = models.CharField(max_length=50, blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test1'

from django.db import models

class Cw2Order(models.Model):
    id = models.IntegerField(primary_key=True)
    avgg = models.FloatField(blank=True, null=True)
    cbm = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    o305 = models.IntegerField(blank=True, null=True)
    o306 = models.IntegerField(blank=True, null=True)
    o307 = models.IntegerField(blank=True, null=True)
    o308 = models.IntegerField(blank=True, null=True)
    o309 = models.IntegerField(blank=True, null=True)
    o342 = models.IntegerField(blank=True, null=True)
    o344 = models.IntegerField(blank=True, null=True)
    o346 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw2_order_data'

