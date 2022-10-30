from django.urls import path
from . import views

urlpatterns = [
   path('api-form/blogs',views.blog_list,name='blog_list'),
   path('form/',views.Form,name='Form'),
   path('show/',views.show,name='show'),
   # path('api-form/blogs/<int:pk>',views.blog_detail,name='blog_detail'),
   path('api-form/blogs/<int:pk>/',views.blog_detail,name='blog_detail'),
   path('show-blog/<int:pk>',views.View_blog,name='View_blog'),
   path('update-blog/<int:pk>',views.Update,name='Update'),
   path('delete-blog/<int:pk>',views.Delete,name='Delete'),
]
