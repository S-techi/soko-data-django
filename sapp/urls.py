from django.urls import path
from . import views

urlpatterns = [
    path('userform/',views.userform,name='display_table'),
    path('displayform/',views.displayform,name='')
]

