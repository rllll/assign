from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from show.models import Choice,UserChoice
import random

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)
def finish(request):
    context = {}
    context['data'] = []
    db = UserChoice.objects.all()
    for user in db:
        user_id = user.uc_user_id
        total_money = user.uc_total_money
        total_saving = user.uc_total_saving
        total_insurance = user.uc_total_insurance
        final_choice = user.uc_final_choice
        integral = user.uc_integral
        obj = Choice.objects.filter(choice_user_id=user_id)
        times = len(obj)
        temp = {
            'user_id':user_id,
            'times':times,
            'total_money':total_money,
            'total_saving':total_saving,
            'total_insurance':total_insurance,
            'final_choice':final_choice,
            'integral':integral
        }
        context['data'].append(temp)
    return render(request,'finish.html',context)
def existsuser(request):
    if request.method == "POST":
        user_id = str(request.POST['user_id'])
        res = {}
        res['user_id'] = user_id
        res['check'] = 0
        try:
            q = UserChoice.objects.get(uc_user_id=user_id)
            res['check'] = 1
        except UserChoice.DoesNotExist:
            res['check'] = 0
        return JsonResponse(res)
def adduser(request):
    if request.method == "POST":
        user_id = str(request.POST['user_id'])
        total_money = float(request.POST['total_money'])
        total_saving = float(request.POST['total_saving'])
        total_insurance = float(request.POST['total_insurance'])
        try:
            q = UserChoice.objects.get(uc_user_id=user_id)
            q.uc_total_money = total_money
            q.uc_total_saving = total_saving
            q.uc_total_insurance = total_insurance
            q.save()
        except UserChoice.DoesNotExist:
            db = UserChoice(uc_user_id=user_id,uc_total_money=total_money,uc_total_saving=total_saving,uc_total_insurance=total_insurance)
            db.save()
        resdata = {}
        resdata['url'] = "/show/ex/" + user_id
        return JsonResponse(resdata)

def experiment(request,user_id):
    context = {
        "tag":0,
        "user_id":user_id,
        "times":1,
        "t_area":0.0,
        "last_remain":0.00,
        "last_choice":"",
        "ex_introduce":"接下来您将有八次机会分配该账户中的钱，每次分配的金额为20（元/亩）。您有一定的概率遭受灾害，请根据每次账户余额，调整下一次分配比重。",
        "data":[]
    }
    try:
        db = Choice.objects.all().filter(choice_user_id=user_id)
        context['tag'] = 1
        context['times'] = len(db) + 1
        for item in db:
            temp = {}
            temp['user_id'] = item.choice_user_id
            temp['ex_times'] = item.choice_times
            temp['area'] = item.choice_area
            context['t_area'] = temp['area']
            temp['saving'] = item.choice_saving
            temp['insurance'] = item.choice_insurance
            temp['lost_situation'] = item.choice_lost_situation
            temp['gain_money'] = item.choice_gain_money
            temp['current_remain'] = item.choice_current_remain
            temp['reduce_money'] = item.choice_reduce_money
            temp['balance'] = item.choice_balance
            context['last_remain'] = temp['balance']
            temp['total_balance'] = item.choice_total_balance
            context['data'].append(temp)
    except Choice.DoesNotExist:
        context['tag'] = 0
    if context['times'] == 9:
        try:
            uc = UserChoice.objects.get(uc_user_id=user_id)
            if uc.uc_final_choice:
                context['last_choice'] = uc.uc_final_choice
                context['times'] += 1
        except UserChoice.DoesNotExist:
            context['last_choice'] = ""
    return render(request,'experiment.html',context)

def addexper(request):
    money_intitial = 20 #初始投入金额(元)
    saving_profits = 1.35 #储蓄利润(%)
    saving_year_profits = 1.75
    product_cycle = 3 #产品周期(月)
    premium_rate = 7.0 #保险费率(%)
    current_savings_rate = 0.55/100.0 #活期储蓄利率

    saving_profits /= 100.0
    saving_year_profits /= 100.0
    product_cycle /= 12.0
    premium_rate /= 100.0

    user_id = str(request.POST['user_id'])
    ex_times = int(request.POST['ex_times'])
    if ex_times <= 8:
        last_remain = float(request.POST['last_remain']) #账户余额
        area = float(request.POST['area']) #亩
        saving = float(request.POST['saving']) #储蓄金额
        insurance = float(request.POST['insurance']) #保险金额
        lost_situation = request.POST['lost_situation']
        affected_degree = float(request.POST['affected_degree']) #受灾程度0-0.7
        gain_money = float(request.POST['gain_money']) #赔偿金额
        affected_date = int(request.POST['affected_date']) #受灾日期
        before_affected_saving_sum = float(request.POST['before_affected_saving_sum'])
        current_remain = float(request.POST['current_remain'])
        is_get = request.POST['is_get'] #是否取出钱
        reduce_money = 0.00 #取出金额
        if is_get == "1":
            is_get = "是"
            reduce_money = float(request.POST['reduce_money'])
        else:
            is_get = "否"
        # 受灾后至产品周期结束账户内金额的本息和
        after_affected_sum = (current_remain-reduce_money)*(1+current_savings_rate*(90-affected_date)*(1/365.0))
        balance = after_affected_sum*(1+1.65/100.0*(9/12)) #账户余额
        total_balance = balance * area #账户总余额

        area = round(area,1)
        # 保留两位小数
        saving = round(saving,2)
        insurance = round(insurance,2)
        affected_degree = round(affected_degree,2)
        gain_money = round(gain_money,2)
        before_affected_saving_sum = round(before_affected_saving_sum,2)
        current_remain = round(current_remain,2)
        reduce_money = round(reduce_money,2)
        after_affected_sum = round(after_affected_sum,2)
        balance = round(balance,2)
        total_balance = round(total_balance,2)
        db = Choice(
            choice_user_id=user_id,
            choice_times=ex_times,
            choice_area=area,
            choice_saving=saving,
            choice_insurance=insurance,
            choice_lost_situation=lost_situation,
            choice_affected_degree=affected_degree,
            choice_gain_money=gain_money,
            choice_affected_date=affected_date,
            choice_before_affected_saving_sum=before_affected_saving_sum,
            choice_current_remain=current_remain,
            choice_is_get=is_get,
            choice_reduce_money=reduce_money,
            choice_after_affected=after_affected_sum,
            choice_balance=balance,
            choice_total_balance=total_balance
        )
        db.save()
    else:
        final_choice = str(request.POST['final_choice'])
        integral = int(request.POST['integral'])
        uc = UserChoice.objects.get(uc_user_id=user_id)
        uc.uc_final_choice = final_choice
        uc.uc_integral = integral
        uc.save()
    return HttpResponseRedirect(reverse('show:exper',kwargs={'user_id':user_id}))