# Generated by Django 3.2.3 on 2021-05-30 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210530_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderform',
            name='product',
        ),
    ]
