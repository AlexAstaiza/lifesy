# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Decodificador(models.Model):
    lenguajecol = models.CharField(max_length=45)
    detectordemovimiento = models.ForeignKey('Detectordemovimiento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'decodificador'


class Detectordemovimiento(models.Model):
    lenguajecol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'detectordemovimiento'


class Discapacidad(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    tdiscapacidad_idtdiscapacidad = models.ForeignKey('Tdiscapacidad', models.DO_NOTHING, db_column='tdiscapacidad_idtdiscapacidad')
    metodos_idmetodos = models.ForeignKey('Metodosdecomunicacion', models.DO_NOTHING, db_column='metodos_idmetodos')

    class Meta:
        managed = False
        db_table = 'discapacidad'
        unique_together = (('id', 'metodos_idmetodos', 'tdiscapacidad_idtdiscapacidad'),)
        db_table_comment = 'Esta es la entidad que gurdara la informacion de la persona encargada de cuidar al paciente '


class EnfermedadDiscapacidad(models.Model):
    enfermedades = models.ForeignKey('Enfermedades', models.DO_NOTHING)
    discapacidad = models.ForeignKey(Discapacidad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enfermedad_discapacidad'
        unique_together = (('id', 'enfermedades', 'discapacidad'),)


class Enfermedades(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    tenfermedades = models.ForeignKey('Tenfermedades', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enfermedades'
        unique_together = (('id', 'tenfermedades'),)


class FacturaCabeza(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    personas_idpersonas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='personas_idpersonas')

    class Meta:
        managed = False
        db_table = 'factura_cabeza'


class FacturaCuerpo(models.Model):
    cantidad = models.IntegerField()
    valor = models.FloatField()
    formasdeadquisicion = models.ForeignKey('Formasdeadquisicion', models.DO_NOTHING)
    factura_cabeza = models.ForeignKey(FacturaCabeza, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'factura_cuerpo'
        unique_together = (('id', 'formasdeadquisicion', 'factura_cabeza'),)


class Formasdeadquisicion(models.Model):
    nombre = models.CharField(max_length=45)
    fechainicial = models.DateField(db_column='fechaInicial')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='fechaFinal')  # Field name made lowercase.
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'formasdeadquisicion'


class Genero(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Historial(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField()
    oraciones = models.ForeignKey('Oraciones', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'historial'
        unique_together = (('id', 'oraciones'),)


class Imagen(models.Model):
    rutaimagen = models.TextField()
    oraciones = models.ForeignKey('Oraciones', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'imagen'
        unique_together = (('id', 'oraciones'),)


class MetodosDePagos(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    factura_cabeza = models.ForeignKey(FacturaCabeza, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'metodos de pagos'
        unique_together = (('id', 'factura_cabeza'),)


class Metodosdecomunicacion(models.Model):
    nombre = models.CharField(max_length=45, db_comment='en este campo se nombra el metodo a trabajar ejemplo: visual, pictograma, historial de oraciones')
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    decodificador = models.ForeignKey(Decodificador, models.DO_NOTHING)
    tmetodosdecomunicacion = models.ForeignKey('Tmetodosdecomunicacion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'metodosdecomunicacion'
        unique_together = (('id', 'decodificador', 'tmetodosdecomunicacion'),)


class Oraciones(models.Model):
    oracion = models.CharField(max_length=255)
    metodosdecomunicacion = models.ForeignKey(Metodosdecomunicacion, models.DO_NOTHING)
    metodosdecomunicacion_tmetodos_idmetodos1 = models.IntegerField(db_column='metodosdecomunicacion_Tmetodos_idmetodos1')  # Field name made lowercase.
    metodosdecomunicacion_decodificador_idlenguaje = models.IntegerField(db_column='metodosdecomunicacion_Decodificador_idlenguaje')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oraciones'
        unique_together = (('id', 'metodosdecomunicacion', 'metodosdecomunicacion_tmetodos_idmetodos1', 'metodosdecomunicacion_decodificador_idlenguaje'),)


class Palabras(models.Model):
    palabra = models.CharField(max_length=45)
    oraciones = models.ForeignKey(Oraciones, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'palabras'
        unique_together = (('id', 'oraciones'),)


class Personas(models.Model):
    nombre1 = models.CharField(max_length=45)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=145, blank=True, null=True)
    celular = models.CharField(max_length=145, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    n_identificacion = models.CharField(max_length=20)
    genero_idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero_idgenero')
    tpersona_idtpersona = models.ForeignKey('Tpersona', models.DO_NOTHING, db_column='tpersona_idtpersona')
    t_documento = models.ForeignKey('TDocumento', models.DO_NOTHING)
    discapacidad = models.ForeignKey(Discapacidad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'personas'
        unique_together = (('id', 't_documento', 'tpersona_idtpersona', 'genero_idgenero', 'discapacidad'),)


class TDocumento(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_documento'


class Tdiscapacidad(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tdiscapacidad'


class Tenfermedades(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenfermedades'


class Tmetodosdecomunicacion(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmetodosdecomunicacion'


class Tpersona(models.Model):
    nombre = models.CharField(max_length=45, db_comment='Estecampo es para nombrar laclasificacionde la categoria, ejemplo: Familiar, Paciente, cuidador')
    descricpcion = models.CharField(max_length=45, blank=True, null=True, db_comment='este campoes para generar una descripcion detallada.')

    class Meta:
        managed = False
        db_table = 'tpersona'
        db_table_comment = 'Esta entidad me permite clasificar las personas de la tabla persona,en pacientes, familiar y cuidador'
