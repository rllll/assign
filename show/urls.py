from django.urls import path

from . import views

app_name = 'show'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.adduser,name='adduser'),
    path('ex/<user_id>',views.experiment,name='exper'),
    path('addex/',views.addexper,name='addex'),
    path('finish/',views.finish,name='finish'),
    path('exists/',views.existsuser,name='exists'),
    path('modify/',views.modifyGL,name='modify')
]