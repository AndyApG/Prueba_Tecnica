# Generated by Django 4.2.14 on 2024-07-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Marca', max_length=20)),
                ('modelo', models.CharField(help_text='Modelo', max_length=20)),
                ('placa', models.CharField(help_text='Placa', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(help_text='Número de documento', max_length=50)),
                ('nombre', models.CharField(help_text='Nombre', max_length=20)),
                ('apellidos', models.CharField(help_text='Apellidos', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ini_cont', models.DateField(help_text='Inicio de contrato')),
                ('cuota', models.FloatField(help_text='Cuota Semanal')),
                ('auto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.auto')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.cliente')),
            ],
            options={
                'ordering': ['ini_cont'],
            },
        ),
    ]
