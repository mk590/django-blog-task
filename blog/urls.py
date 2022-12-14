from django.urls import path
from . import views

urlpatterns = [
   path('api-form/blogs',views.blog_list,name='blog_list'),
   path('form/',views.Form,name='Form'),
   path('new_user/',views.Add_User,name='Add_User'),
   path('show/',views.show,name='show'),
   # path('api-form/blogs/<int:pk>',views.blog_detail,name='blog_detail'),
   path('api-form/blogs/<int:pk>/',views.blog_detail,name='blog_detail'),
   path('update-blog/<int:pk>',views.Update,name='Update'),
   path('delete-blog/<int:pk>',views.Delete,name='Delete'),
]
