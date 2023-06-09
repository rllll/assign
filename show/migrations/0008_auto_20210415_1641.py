# Generated by Django 3.1.6 on 2021-04-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0007_choice_choice_is_get'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_final_value',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_remain_saving_gain',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_saving_gain',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_affected_date',
            field=models.IntegerField(blank=True, null=True, verbose_name='受灾日期'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_affected_degree',
            field=models.FloatField(blank=True, null=True, verbose_name='受灾程度'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_after_affected',
            field=models.FloatField(blank=True, null=True, verbose_name='受灾后至产品周期结束账户内金额的本息和'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_before_affected_saving_sum',
            field=models.FloatField(blank=True, null=True, verbose_name='受灾前储蓄本息和'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_current_remain',
            field=models.FloatField(blank=True, null=True, verbose_name='受灾时账户余额'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_balance',
            field=models.FloatField(verbose_name='本次账户余额（元/亩）'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_gain_money',
            field=models.FloatField(blank=True, null=True, verbose_name='获得赔偿金额'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_is_get',
            field=models.CharField(max_length=10, verbose_name='是否从账户中取出钱'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_reduce_money',
            field=models.FloatField(verbose_name='取出金额'),
        ),
    ]
