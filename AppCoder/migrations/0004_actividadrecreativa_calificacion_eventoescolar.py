# Generated by Django 5.0.6 on 2024-06-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_entregable_profesor_estudiante_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadRecreativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=40)),
                ('nota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventoEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
    ]