from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hello_list,name='abc'),
    path('a/<int:wow>/', views.Hello_detail,name='def'),
]
