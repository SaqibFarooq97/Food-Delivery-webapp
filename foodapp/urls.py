from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', main_view, name='main_view'),
    path('students', students, name='students'),
    path('login',login,name='login'),
    # path('registration',registration,name='registration'),
    path('check',check,name='check'),
    path('student_details/<reg_no>', student_details, name='student_details'),
    path('food_descriptions/<food_des>', food_descriptions, name='food_descriptions'),
    # path('registar',registar,name='registar'),
    path('order/<rest_id>', order, name='order'),
    path('registrations', registrations, name='registrations'),
    path('newsignup', newsignup, name='newsignup'),
    path('addcatageory', addcatageory, name='addcatageory'),
    path('restaurent', restaurent, name='restaurent'),
    path('users', users, name='users'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('cart', cart, name='cart'),
    path('orders', orders, name='orders'),
    path('logout', logout, name='logout'),
    path('add_item', add_item, name='add_item'),
    path('dashboard/<result_id>', dashboard, name='dashboard'),
    path('status_check',status_check,name='status_check'),
    path('remove_item',remove_item,name='remove_item'),
    path('sucess',sucess,name='sucess'),
    path('myOrders',myOrders,name='myOrders'),
    path('edit_item',edit_item,name='edit_item'),
    path('files',files,name='files'),
    path('login_page',login_page,name='login_page'),
    path('remove_menu',remove_menu,name='remove_menu'),
    path('auto_complete',auto_complete,name='auto_complete'),
    path('view_restaurant',view_restaurant,name='view_restaurant')
    


    




 
 

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)