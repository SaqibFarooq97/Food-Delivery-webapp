from django.contrib import admin
from .models import  Students,file_upload, Course,Signup,Cart, CartItem, Add_Products, Users, allusers, Add_catageory, register,AppUser, food_items ,Newsignup, Menu,Customer#OrderDetails,AppUser, Order, User  #Item,OrderItem,Cart
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ("code" , "name")
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):

    list_display = ("name", "registration_no",)

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email' , 'user_type','password')


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):

    list_display = ('username', 'email' , 'user_type','password', 'address')    
@admin.register(register)
class registerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'password','address','city','state','zip')

#  @admin.register(registar)
# class registorAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'email', 'password','address','type')


# @admin.register(allusers)
# class allusersAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'email', 'password','address','type')


@admin.register(food_items)
class food_itemsAdmin(admin.ModelAdmin):

    list_display = ('food_name', 'food_description', 'category','item_price', 'item_image','item_ingredents' )    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('item_no', 'item_name' ,'item_image','item_ingredients','item_price','item_description')    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_first_name','customer_last_name','customer_phone_no','customer_username','customer_password','customer_email')    

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):

#     list_display = ('full_name','contact','email_address','username','password' ) 

# @admin.register(Order)
# class Order(admin.ModelAdmin):

#    list_display = ('order_id', 'customer_id','quantity','date' )           


# @admin.register(OrderDetails)
# class OrderDetails(admin.ModelAdmin):

#     list_display = ('order_details_id', 'order_id','menu_id','amount','no_of_orders','total_amount' )    
@admin.register(Newsignup)
class NewsignupAdmin(admin.ModelAdmin):

    list_display = ('username', 'email' ,'password', 'address','restaurentname','restaurentspeaciality', 'restaurentimage')    

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):

    list_display = ('username', 'email' ,'password', 'address')    

@admin.register(Add_Products)
class Add_ProductsAdmin(admin.ModelAdmin):

    list_display = ('catageory_name', 'item_name' ,'item_image','item_ingredents','item_price',)    



# admin.site.register(Add_catageory)
@admin.register(Add_catageory) 
class Add_catageoryAdmin(admin.ModelAdmin):

    list_display = ('catageory',) 


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('id','user', 'grand_total')  

@admin.register(file_upload)
class file_uploadAdmin(admin.ModelAdmin):

    list_display = ('item_image','item_name')  

# @admin.register(Save_cart)
# class Save_cartAdmin(admin.ModelAdmin):

#     list_display = ()  


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = ('item', 'quantity','added_to_cart',)    




# @admin.register(Profile)   
# class ProfileAdmin(admin.ModelAdmin):

#     list_display = ('res_img', 'speaciality')        
       

# admin.site.register(Students)
# admin.site.register(Course)
# admin.site.register(Order)
# admin.site.register(Customer)
# admin.site.register(Item)
# admin.site.register(OrderItem)
# admin.site.register(Cart)
# admin.site.register(Menu)



