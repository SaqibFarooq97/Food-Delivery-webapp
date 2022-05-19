from django.db import models
from django import forms

# Create your models here.

ORDER_STATUS_CHOICES = (
    ('NEW','NEW'),
    ('CONFIRMED', 'CONFIRMED'),
    ('PROCESSING','PROCESSING'),
    ('OUT FOR DELIVARY','OUT FOR DELIVARY'),
    ('DELIVERED','DELIVERED'),
    ('CANCELLED', 'CANCELLED'),
    ('RETURNED', 'RETURNED'),
)

class Course(models.Model):

    name = models.CharField('Course Name',max_length=300)
    code = models.CharField('Course Code',max_length=6)


    def __str__(self):
        return self.name




class AppUser(models.Model):

    username = models.CharField('username', max_length=300)
    email = models.EmailField('email')
    password = models.CharField('password',max_length=300)
    user_type = models.CharField(max_length=100, choices = (('Admin',"Administrator"), ('User','User')), default='User')


class Signup(models.Model):

    username = models.CharField('username', max_length=300)
    email = models.EmailField('email')
    password = models.CharField('password',max_length=300)
    address = models.CharField('address', max_length=300)
    user_type = models.CharField(max_length=100, choices = (('Admin',"Administrator"), ('User','User')), default='User')


class Students(models.Model):

    name = models.CharField('Name',max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_no = models.IntegerField('Registration No')

class Menu(models.Model):
    item_no = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_image = models.ImageField()
    item_ingredients = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=500)


class Customer(models.Model):
    customer_id= models.IntegerField()
    customer_first_name= models.CharField(max_length=20)
    customer_last_name= models.CharField(max_length=20)
    customer_phone_no= models.IntegerField()
    customer_username = models.CharField(max_length=20)
    customer_password = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=20)

# class User(models.Model):
#     user_id= models.IntegerField(default=1)
#     full_name= models.CharField(max_length=20)
#     contact= models.IntegerField()
#     email_address = models.CharField(max_length=20)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)


# class Order(models.Model):
#     order_id = models.IntegerField()
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) #foreign key that links to the customer table. It refers to the customer who ordered the food.
#     quantity = models.IntegerField()
#     date = models.DateTimeField(auto_now_add=True)
#     processed_by = models.CharField(max_length=200)
    # processed_by =models.ForeignKey(User, on_delete=models.CASCADE)#this is a foreign key that connects or links to the user table. It refers to the user who processed the transaction.

# class OrderDetails(models.Model):
#     order_details_id = models.AutoField(primary_key= True)
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     no_of_orders =  models.IntegerField() 
#     total_amount = models.IntegerField() 
    


# class Item(models.Model):
#     name= models.CharField()
#     price= models.IntegerField()
#     description= models.CharField
#     category= models.CharField()
# class OrderItem(models.Model):
#     item= models.ForeignKey(Item,on_delete=models.CASCADE)
#     quantity= models.IntegerField()

# class Cart(models.Model):
#      items= models.ManyToManyField(OrderItem)
#      total= models.IntegerField()
#      discount= models.IntegerField()
#      order_date = models.DateTimeField(auto_now_add=True)

class register(models.Model):
    user_name= models.CharField('Name',max_length=50)
    email= models.CharField('Email', max_length=50)
    password = models.CharField('password', max_length=50)
    address = models.CharField('Address', max_length=50)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    zip = models.IntegerField()


class allusers(models.Model):
    user_name= models.CharField('Name',max_length=50)
    email= models.CharField('Email', max_length=50)
    password = models.CharField('password', max_length=50)
    address = models.CharField('Address', max_length=50)
    
class Add_catageory(models.Model):
    catageory = models.CharField('catageory', max_length=40)
     


class Users(models.Model):
    username = models.CharField('username', max_length=300, null=True, blank=True)
    email = models.EmailField('email')
    password = models.CharField('password',max_length=300)
    address = models.CharField('address', max_length=300,null=True, blank=True)

class Newsignup(models.Model):
    restaurentname = models.CharField('restaurentname', max_length=300, null=True, blank=True)
    username = models.CharField('username', max_length=300, null=True, blank=True)
    email = models.EmailField('email')
    password = models.CharField('password',max_length=300)
    address = models.CharField('address', max_length=300,null=True, blank=True)
    restaurentspeaciality = models.CharField('restaurentspeaciality', max_length=300, null=True, blank=True)
    restaurentimage = models.ImageField(upload_to="images",null=True, blank=True)
    # items = models.(food_items, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, to_field="email", on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurentname

class food_items(models.Model):
    food_name = models.CharField('food_name',max_length=50)
    food_description = models.CharField('food_description', max_length=300, null=True, blank=True)
    category = models.CharField('category', max_length=400, null=True, blank=True)
    item_price =  models.CharField('item_price',max_length=300)
    item_image =  models.ImageField(upload_to="images",null=True, blank=True)
    item_ingredents =  models.CharField('item_ingredents',max_length=300)
    restaurent = models.ForeignKey(Newsignup,on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.food_name

class Profile(models.Model):
    
    res_img = models.ImageField()
    speaciality = models.CharField('speaciality',max_length=300)
    # user = models.OneToOneField(Newsignup, on_delete=models.CASCADE,null=True)
class file_upload(models.Model):
    item_image =  models.FileField(upload_to="images",null=True, blank=True)
    item_name = models.CharField('item_name', max_length=100)



class Add_Products(models.Model):
    catageory_name =  models.CharField('catageory_name',max_length=300)
    item_name =  models.CharField('item_name',max_length=300)
    item_price =  models.CharField('item_price',max_length=300)
    item_image =  models.ImageField('item_image',max_length=300)
    item_ingredents =  models.CharField('item_ingredents',max_length=300)


class CartItem(models.Model):
    item = models.ForeignKey(food_items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    added_to_cart = models.BooleanField(default=False)

class Cart(models.Model):

    # order_id = models.AutoField(primary_key=True, default=1)
    items_all = models.ManyToManyField(CartItem)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    grand_total = models.IntegerField()
    address = models.CharField('address',max_length=100)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='NEW')


    # def __str__(self):
    #     return self.order_id

# class Save_cart(models.Model):   
#     items = models.ManyToManyField(CartItem)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     grand_total = models.IntegerField()

#     # def __str__(self):
#     #     return self.items.id     

