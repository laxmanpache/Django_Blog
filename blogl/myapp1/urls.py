
from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='index'),
        
         path('register',views.user_register,name='register'),
        path('login',views.user_login,name='login'),
        path('logout',views.user_logout,name='logout'),
        path('post_blog',views.post_blog,name='post_blog'),
        path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
        path('blog_delete/<int:id>',views.blog_delete,name='blog_delete'),
       
        path('edit/<int:id>',views.edit,name='edit'),






]
