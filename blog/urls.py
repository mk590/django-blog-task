from django.urls import path
from . import views

urlpatterns = [
   path('api-form/blogs',views.blog_list,name='blog_list'),
   path('form/',views.Form,name='Form'),
   path('show/',views.show,name='show'),
]
