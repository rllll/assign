from django.contrib import admin
from .models import Choice,UserChoice

from django.http import HttpResponse

from openpyxl import Workbook

# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    actions = ['export_as_excel']
    def export_as_excel(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename=experiment_data.xlsx'
        wb = Workbook() # 新建Workbook
        ws = wb.active # 使用当前活动的Sheet表
        field_names_ch = ['id','用户编号','当前实验次数','种植水稻的土地面积','储蓄金额','保险金额','受灾赔偿情况','受灾程度','获得赔偿金额','受灾日期','受灾前储蓄本息和','受灾时账户余额','是否从账户中取出钱','取出金额','受灾后至产品周期结束账户内金额的本息和','本次账户余额（元/亩）','账户总余额']
        ws.append(field_names_ch) # 将模型字段名作为标题写入第一行
        for obj in queryset: # 遍历选择的对象列表
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names] # 将模型属性值的文本格式组成列表
            ws.append(data) # 写入模型属性值
        wb.save(response) # 将数据存入响应内容
        return response

    export_as_excel.short_description = "导出为Excel数据"

class UserChoiceAdmin(admin.ModelAdmin):
    actions = ['export_as_excel']
    def export_as_excel(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename=user_data.xlsx'
        wb = Workbook() # 新建Workbook
        ws = wb.active # 使用当前活动的Sheet表
        field_names_ch = ['id','用户编号','愿意投入金额','储蓄愿意投入金额','保险愿意投入金额','用户最终选择','最终积分']
        ws.append(field_names_ch) # 将模型字段名作为标题写入第一行
        for obj in queryset: # 遍历选择的对象列表
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names] # 将模型属性值的文本格式组成列表
            ws.append(data) # 写入模型属性值
        wb.save(response) # 将数据存入响应内容
        return response

    export_as_excel.short_description = "导出为Excel数据"

admin.site.register(Choice,ChoiceAdmin)
admin.site.register(UserChoice,UserChoiceAdmin)