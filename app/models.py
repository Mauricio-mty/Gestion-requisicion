# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class areaEmpleado(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombrearea = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areaempleado'


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


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(primary_key=True)
    fechacotizacion = models.DateField(blank=True, null=True)
    fechaentrega = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    idrequisicion = models.ForeignKey('Requisicion', models.DO_NOTHING, db_column='idrequisicion', blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizacion'


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


class Empleado(models.Model):
    idempleado = models.AutoField(primary_key=True)
    nombreempleado = models.CharField(max_length=255, blank=True, null=True)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    idarea = models.ForeignKey(areaEmpleado, models.DO_NOTHING, db_column='idarea', blank=True, null=True)
    idtipoempleado = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='idtipoempleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class productosRequisicion(models.Model):
    idproductorequi = models.AutoField(primary_key=True)
    nombreproducto = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=80, blank=True, null=True)
    idrequisicion = models.ForeignKey('Requisicion', models.DO_NOTHING, db_column='idrequisicion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosrequisicion'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombreproveedor = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombrecontacto = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    idtipoproveedor = models.ForeignKey('Tipoproveedor', models.DO_NOTHING, db_column='idtipoproveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Requisicion(models.Model):
    idrequisicion = models.AutoField(primary_key=True)
    numeroserie = models.IntegerField(blank=True, null=True)
    fechageneracion = models.DateField(blank=True, null=True)
    fechaentrega = models.DateField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion'


class tipoEmpleado(models.Model):
    idtipoempleado = models.AutoField(primary_key=True)
    nombretipo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoempleado'


class tipoProveedor(models.Model):
    idtipoproveedor = models.AutoField(primary_key=True)
    nombretipoproveedor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoproveedor'
