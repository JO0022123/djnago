from .import views
from django.urls import path
from django.urls import re_path as url
urlpatterns=[
    path('',views.home,name="home"),  
    path("index/",views.index,name="index"),
     path("reg/",views.reg,name="reg"),
      path("login/",views.login,name="login"),
   
    path('create',views.create,name="create"),
    url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
     path('retrieve/',views.retrieve,name="retrieve"),
     path('edit/<int:id>',views.edit,name="edit"),
     path('update/<int:id>',views.update,name="update"),
     path('product/',views.product,name="product"),
   
]