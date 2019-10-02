# Generated by Django 2.2 on 2019-07-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentacion', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('dificultad', models.CharField(max_length=6)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wans.Cliente')),
            ],
        ),
    ]