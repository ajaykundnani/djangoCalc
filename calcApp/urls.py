
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ans/<int:c>',views.ans,name='ans'),
]