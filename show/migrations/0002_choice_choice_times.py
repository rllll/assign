# Generated by Django 3.1.6 on 2021-04-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_times',
            field=models.CharField(default=-1, max_length=50, verbose_name='当前实验次数'),
            preserve_default=False,
        ),
    ]
