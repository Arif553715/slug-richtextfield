# Generated by Django 2.2.1 on 2019-06-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20190603_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]