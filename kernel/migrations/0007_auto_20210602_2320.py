# Generated by Django 3.1.7 on 2021-06-02 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0006_auto_20210602_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estatusproveedor',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
