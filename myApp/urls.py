from django.urls import path
from . import views

urlpatterns=[
    
    path('userinput',views.formy,name='homeb  '),
    path('displayinput',views.displayinput,name='table'),
    path('one/<str:pk>',views.one,name='one'),
    path('update/<str:pk>',views.update,name='update')
]