# Generated by Django 3.1.6 on 2021-04-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_choice_choice_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='uc_integral',
            field=models.FloatField(default=0.0, verbose_name='最终积分'),
            preserve_default=False,
        ),
    ]