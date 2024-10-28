# Generated by Django 4.2.4 on 2023-08-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='AdrClient',
            field=models.CharField(default='Menabe', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='NomClient',
            field=models.CharField(default='Michel', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='NumClient',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]