from django.urls import path
from .views import item_list

app_name = 'buyX'

urlpatterns = [
    path('', item_list, name='item_list')
]
