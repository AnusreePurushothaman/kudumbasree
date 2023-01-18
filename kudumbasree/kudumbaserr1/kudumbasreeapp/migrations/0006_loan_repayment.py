# Generated by Django 3.0.3 on 2020-02-25 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudumbasreeapp', '0005_auto_20200225_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan_repayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_repay', models.IntegerField()),
                ('date', models.CharField(default='', max_length=100)),
                ('loanid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='kudumbasreeapp.loan')),
            ],
        ),
    ]