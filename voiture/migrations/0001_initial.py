# Generated by Django 4.1 on 2022-09-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marque', models.CharField(max_length=200, null=True)),
                ('Pu', models.FloatField(null=True)),
                ('StockActuel', models.FloatField(null=True)),
                ('StockInit', models.FloatField(null=True)),
            ],
        ),
    ]
