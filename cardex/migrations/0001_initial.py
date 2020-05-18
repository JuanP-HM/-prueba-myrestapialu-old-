# Generated by Django 3.0.6 on 2020-05-06 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('no_control', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
                ('carrera', models.CharField(max_length=32)),
                ('foto', models.ImageField(upload_to='fotos-alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('clave', models.CharField(max_length=6)),
                ('no_semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=6)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('alumnos', models.ManyToManyField(blank=True, to='cardex.Alumno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardex.Materia')),
            ],
        ),
    ]
