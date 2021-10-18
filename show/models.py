from django.db import models

# Create your models here.
class Choice(models.Model):
    choice_id = models.AutoField(verbose_name="选择id",primary_key=True)
    choice_user_id = models.CharField(max_length=100,verbose_name="用户编号")
    choice_times = models.IntegerField(verbose_name="当前实验次数")
    choice_area = models.FloatField(verbose_name="种植水稻的土地面积")
    choice_saving = models.FloatField(verbose_name="储蓄金额")
    choice_insurance = models.FloatField(verbose_name="保险金额")
    choice_lost_situation = models.CharField(max_length=20,verbose_name="受灾赔偿情况")
    choice_affected_degree = models.FloatField(verbose_name="受灾程度",null=True,blank=True)
    choice_gain_money = models.FloatField(verbose_name="获得赔偿金额",null=True,blank=True)
    choice_affected_date = models.IntegerField(verbose_name="受灾日期",null=True,blank=True)
    choice_before_affected_saving_sum = models.FloatField(verbose_name="受灾前储蓄本息和",null=True,blank=True)
    choice_current_remain = models.FloatField(verbose_name="受灾时账户余额",null=True,blank=True)
    choice_is_get = models.CharField(max_length=10,verbose_name="是否从账户中取出钱")
    choice_reduce_money = models.FloatField(verbose_name="取出金额")
    choice_after_affected = models.FloatField(verbose_name="受灾后至产品周期结束账户内金额的本息和",null=True,blank=True)
    choice_balance = models.FloatField(verbose_name="本次账户余额（元/亩）")
    choice_total_balance = models.FloatField(verbose_name="账户总余额")
    class Meta:
        verbose_name="实验记录"
        verbose_name_plural="实验记录"

class UserChoice(models.Model):
    uc_id = models.AutoField(verbose_name="id",primary_key=True)
    uc_user_id = models.CharField(max_length=100,verbose_name="用户编号")
    uc_total_money = models.FloatField(verbose_name="愿意投入金额")
    uc_total_saving = models.FloatField(verbose_name="储蓄愿意投入金额")
    uc_total_insurance = models.FloatField(verbose_name="保险愿意投入金额")
    uc_final_choice = models.CharField(max_length=100,verbose_name="用户最终选择",blank=True,null=True)
    uc_integral = models.FloatField(verbose_name="最终积分",blank=True,null=True)
    class Meta:
        verbose_name="所有用户"
        verbose_name_plural="所有用户"