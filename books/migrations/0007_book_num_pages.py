# Generated by Django 2.1b1 on 2018-07-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20180719_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
