# Generated by Django 3.0.3 on 2020-02-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudumbasreeapp', '0004_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='applidate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loaner',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='remarks',
            field=models.CharField(default='', max_length=50),
        ),
    ]
