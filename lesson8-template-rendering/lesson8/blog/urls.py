from django.conf.urls import url
from django.contrib import admin


from views import post_model_list_view

urlpatterns = [
    url(r'^list/', post_model_list_view, name='list')
]