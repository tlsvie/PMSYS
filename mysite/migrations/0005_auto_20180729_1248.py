# Generated by Django 2.1b1 on 2018-07-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20180729_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product1',
            name='year',
            field=models.PositiveIntegerField(default=2018, verbose_name='出厂年份'),
        ),
    ]
