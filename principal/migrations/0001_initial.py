# Generated by Django 4.2.1 on 2023-05-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decodificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguajecol', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'decodificador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detectordemovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguajecol', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'detectordemovimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'discapacidad',
                'db_table_comment': 'Esta es la entidad que gurdara la informacion de la persona encargada de cuidar al paciente ',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EnfermedadDiscapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'enfermedad_discapacidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'enfermedades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacturaCabeza',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'factura_cabeza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacturaCuerpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
            options={
                'db_table': 'factura_cuerpo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formasdeadquisicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('fechainicial', models.DateField(db_column='fechaInicial')),
                ('fechafinal', models.DateField(db_column='fechaFinal')),
                ('valor', models.FloatField()),
            ],
            options={
                'db_table': 'formasdeadquisicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'genero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'historial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutaimagen', models.TextField()),
            ],
            options={
                'db_table': 'imagen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metodosdecomunicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='en este campo se nombra el metodo a trabajar ejemplo: visual, pictograma, historial de oraciones', max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'metodosdecomunicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetodosDePagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'metodos de pagos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oraciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oracion', models.CharField(max_length=255)),
                ('metodosdecomunicacion_tmetodos_idmetodos1', models.IntegerField(db_column='metodosdecomunicacion_Tmetodos_idmetodos1')),
                ('metodosdecomunicacion_decodificador_idlenguaje', models.IntegerField(db_column='metodosdecomunicacion_Decodificador_idlenguaje')),
            ],
            options={
                'db_table': 'oraciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Palabras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'palabras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=45)),
                ('nombre2', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido1', models.CharField(max_length=45)),
                ('apellido2', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=145, null=True)),
                ('celular', models.CharField(blank=True, max_length=145, null=True)),
                ('fechanacimiento', models.DateField(blank=True, null=True)),
                ('n_identificacion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tdiscapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tdiscapacidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 't_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tenfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tenfermedades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tmetodosdecomunicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tmetodosdecomunicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tpersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='Estecampo es para nombrar laclasificacionde la categoria, ejemplo: Familiar, Paciente, cuidador', max_length=45)),
                ('descricpcion', models.CharField(blank=True, db_comment='este campoes para generar una descripcion detallada.', max_length=45, null=True)),
            ],
            options={
                'db_table': 'tpersona',
                'db_table_comment': 'Esta entidad me permite clasificar las personas de la tabla persona,en pacientes, familiar y cuidador',
                'managed': False,
            },
        ),
    ]