# Generated by Django 2.2.1 on 2019-06-03 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20190603_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Currency'),
        ),
    ]
