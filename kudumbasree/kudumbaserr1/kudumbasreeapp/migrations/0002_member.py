# Generated by Django 3.0.3 on 2020-02-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudumbasreeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('remarks', models.CharField(default='', max_length=100)),
            ],
        ),
    ]