# Generated by Django 4.1.3 on 2022-11-30 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=30)),
                ('arrivee', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('date', models.CharField(max_length=30)),
                ('heure', models.CharField(max_length=15)),
                ('compagnie', models.ManyToManyField(to='appReserv.compagnie')),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appReserv.trajet')),
            ],
        ),
    ]