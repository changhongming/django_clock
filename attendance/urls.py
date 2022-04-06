from django.urls import path
from . import views 

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.result, name='result'),
    path('result/', views.result, name='result'),
    path('test1/test/',views.test,name='test'),
]