# Generated by Django 3.0.7 on 2020-06-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20200620_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date ended',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='date started'),
        ),
    ]