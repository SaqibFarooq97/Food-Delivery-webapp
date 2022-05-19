from django.shortcuts import render
from .models import Students , Course,file_upload, CartItem,Cart, AppUser,register,food_items,Signup,Newsignup,Profile,Add_catageory, Users
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
import json
import requests
import random
from datetime import datetime 
from pprint import pprint
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from django.contrib.auth import logout


# Create your views here.
from django.http import HttpResponse
from django.db.models.query import QuerySet


def logout_view(request):
     logout(request)
     return render(request,"index.html")


def main_view(request):
     

     if request.session.get("email",False):

          print("session of ",request.session["email"])
          user_id = request.session["user_id"]
          user = Users.objects.get(pk=user_id)
          user = request.session["email"]
          # print('name', user.username)
          return render(request,"index.html", {'valid_user':user})
     else:
          return render(request,"index.html")



def students(request):

     if request.method == "POST":
          print("POST REQUEST")
          print(request.POST)
          name = request.POST.get('name')
          phno = request.POST.get('number')

          print (name, phno)



     

     print(mca_students)

     return render(request, 'main.html', {"std":mca_students})

def food_descriptions(request, food_des):
     foods = food_items.objects.get(food_name=food_des)
     print(foods.id)
     return render(request, 'food_description.html',{"food":foods})     


def view_restaurant(request):
     if request.session.get("email",False):

     
     
          request.method == "POST"
          searched_restaurant = request.POST.get('search')
          objct = Newsignup.objects.get(restaurentname =searched_restaurant )

          
          print("restaurent id",objct.id)
          id_rest = objct.id
          return redirect('order', rest_id=id_rest)
     else:
          return render(request, 'logins.html' )




def student_details(request, reg_no):

     std = Students.objects.get(registration_no=reg_no)

     return render(request, 'std_details.html',{"student":std})

def files(request):
     if request.method == "POST":

          items=file_upload()
     
          items.item_image = request.FILES.get('item_image')
          items.item_name = request.POST.get('item_name')
          items.save()
          return render(request, 'additem.html')

def auto_complete(request):
     print(request.GET)
     query_orginal = request.GET.get('term')
     queryset = Newsignup.objects.filter(restaurentname__icontains=query_orginal)
     my_list = []
     my_list += [x.restaurentname for x in queryset]
     return JsonResponse(my_list, safe= False)

def get_cust_orders(session):

     user_id = session["user_id"]
     user = Users.objects.get(pk=user_id)
     cart_items = CartItem.objects.filter(ordered_by=user, order_date__date= datetime.now().date())
     print(">>>>>>>>>", cart_items)
     #Returns Set instead of List {} set([]) 
     print({item.item.restaurent.id for item in cart_items})
     return {item.item.restaurent.id for item in cart_items}

def order(request, rest_id):  


     print(">>>", type(rest_id)) 
     flag = False


     cust_orders  = get_cust_orders(request.session)
     #set of id cust_orders

     if int(rest_id) not in cust_orders:
          flag = True
     
     rest_name=Newsignup.objects.get(pk=int(rest_id))

     items = food_items.objects.filter(restaurent=rest_name.id)
     print(">>>>>>",items)
     # categories = {item.category.lower() for item in items}
     categories = {item.category.lower() for item in items}
     # print(">>>> ", categories)
     prices = {item.item_price for item in items}
     print(">>>> ", prices)
     to_display ={}
     for category in categories:

          to_display[category] = [item for item in items if item.category.lower() == category]
          

     print(to_display)
     
     # to_print ={}
     # for price in prices:
     #      to_print[price] = [item for item in items if item.category == price]

     # print(to_print)
     uemail = str(request.session["email"])
     user = Users.objects.get(email=uemail)
     
     print("Flag:::>>> ", flag)
     return render(request, 'menus.html',{'restaurent': rest_name, 'all': to_display, "flag": flag ,"user": user})

def restaurent(request):
     if request.session.get("email",False):
          user_id = request.session["user_id"]
          user = Users.objects.get(pk=user_id)
          # user = request.session["email"]
          print('name', user.username)
          owners = Newsignup.objects.exclude(restaurentname__isnull=True)

          return render(request,"list_restaurents.html", {'valid_user':user,'alls':owners})
     else:

          return render(request, 'logins.html' )


def status_check(request):
     # result = Newsignup.objects.get(pk=int(result_id))

     # request.session['res_id'] = result.id
     # request.session['email'] = result.email
     rest_id = int(request.session['res_id'])
     rest  = Newsignup.objects.get(pk=rest_id)


     
     if request.method == "POST":
          item_id = request.POST.get('item_id')
          status = request.POST.get('status')
          print("hiiiii",item_id,status)
          print("hiiiashbjhdfdjii",status)
  
  
          item = Cart.objects.get(pk=int(item_id))
          item.order_status = status
          item.save()
          print('status', item.order_status)
          
     return redirect('dashboard', result_id=rest_id)    
def dashboard(request, result_id):
     rest_id = int(request.session['res_id'])


     result = Newsignup.objects.get(pk=int(result_id))
     name_rest= result.restaurentname
     

     total_orders = Cart.objects.filter(items_all__item__restaurent__pk=result.id).count()
     orders_today = Cart.objects.filter(items_all__item__restaurent__pk=result.id, items_all__order_date__date= datetime.today().date()).count()
     total_items = food_items.objects.filter(restaurent__pk=result.id).count()
     total_catagories =  len({item.category.lower() for item  in food_items.objects.filter(restaurent__pk=result.id)})


     orders = set(Cart.objects.filter(items_all__item__restaurent__pk=result.id))

     print(">>>>>>>>>>>>>. ", len(orders))
          
      # if result.restaurentname:
     return render(request, 'dashboard.html',{'rest_id':rest_id,'res_owner':name_rest, 'total_orders': total_orders, 'orders_today': orders_today, 'total_items': total_items, 'orders':orders,'total_catagories':total_catagories})




def login(request):
        
 
     a=1
     emails= a

     if request.method == "POST":
       
          
          print(">>>>>>>>>>>>> ", request.POST)
          email = request.POST.get('email')
          password = request.POST.get('password')
          
          user=None
          result = None
          result = Newsignup.objects.filter(email=email, password=password).first()
          user= Users.objects.filter(email=email, password=password).first()
          

          if result:
               print("#######", result.email)
               request.session['res_id'] = result.id
               request.session['email'] = result.email


               return redirect('dashboard', result_id=result.id)

             
               
               

          elif user:
               request.session['user_id'] = user.id
               request.session['email'] = user.email
              
               print("Not users", result)
               print(user, user.id)
               owners = Newsignup.objects.exclude(restaurentname__isnull=True)

               return render(request, 'list_restaurents.html', {'valid_user':user, 'alls':owners })
               
          # else:
          #      return render(request, 'logins.html',{'invalid_user':email})
               
          else:
               return render(request, 'logins.html',{'invalid_user':emails})
     else:

          return render(request, 'logins.html')          

# def registar(request):
#      if request.method == "POST":

#           print(request.POST)
#           std=Signup()
#           std.username= request.POST.get('inputname')
#           std.email = request.POST.get('inputemail')
#           std.password = request.POST.get('inputpassword')
#           std.address = request.POST.get('inputaddress')
#           std.user_type = request.POST.get('option')
#           std.save()
#           return render(request, 'logins.html')
     
#      else:
#           return render(request, 'registrations.html')
def newsignup(request):
     if request.method == "POST":

          print(request.POST)
          sig=Newsignup()
          sig.username= request.POST.get('inputname')
          sig.email = request.POST.get('inputemail')
          sig.password = request.POST.get('inputpassword')
          sig.address = request.POST.get('inputaddress')
          sig.restaurentname = request.POST.get('restaurentname')
          sig.restaurentspeaciality = request.POST.get('speaciality')
          sig.restaurentimage = request.POST.get('image')
          

         
          sig.save()
          return render(request, 'logins.html')
     
     else:
          return render(request, 'registrations.html')          
def users(request):
     if request.method == "POST":

          print(request.POST)
          sig=Users()
          sig.username= request.POST.get('inputname')
          sig.email = request.POST.get('inputemail')
          sig.password = request.POST.get('inputpassword')
          sig.address = request.POST.get('inputaddress')
          sig.save()
          return render(request, 'logins.html')
     
     else:
          return render(request, 'registrations.html')  
# def registrations(request):
#      if request.method == "POST":
#           std=register()
#           std.user_name= request.POST.get('inputname')
#           std.email = request.POST.get('inputemail')
#           std.password = request.POST.get('inputpassword')
#           std.address = request.POST.get('inputaddress')
#           std.type = request.POST.get('inputoption')
#           std.save()
#           return render(request, 'logins.html')          

def check(request):
     if request.method == "POST":
          name = request.POST.get('username')
          usertype = request.POST.get('user_type')
          user = AppUser.objects.filter(username=name, user_type=usertype)
          if user:

               return render(request, 'main.html', {'is_user': user})
          else:

               return render(request, 'sucess.html')


# def food_list(request):
#       food_variety = food_items.food_name()
#       return render(request, 'main.html',{'food': food_variety})



def registrations():

     return render(request,'registrations.html')

def login_page(request):

     return render(request,'logins.html')       
    


def add_item(request):
     rest_id = int(request.session['res_id'])
     rest  = Newsignup.objects.get(pk=rest_id)


     if request.method == "POST":

          catagories = food_items.objects.all()
          # for item in catagories:
          #      print("cat",item.category)
         
          cat = set()
          
         
     
     # request.session['email'] = result.email
     # if request.method == "POST":

          rest_id = int(request.session['res_id'])

          rest  = Newsignup.objects.get(pk=rest_id)
          items = food_items()
          items.food_name= request.POST.get('item_name')
          items.item_price = request.POST.get('item_price')
          items.item_image = request.FILES.get('item_image')
          
          cats = request.POST.get('catageory_name')
          for item in catagories:

               if item.category  not in cat:
                    items.category=cats
               
                    cat.add(items.category)

          items.item_ingredents = request.POST.get('itemingredents')
          items.food_description = request.POST.get('itemdes')
          items.restaurent = rest
          items.save()



     return render(request, 'additem.html', {'rest_id' : rest_id,'res_owner':rest}) 

        
def profile():
      if request.method == "POST":

          print(request.POST)
          prof=Profile()
          prof.res_img= request.POST.get('image')
          prof.speaciality = request.POST.get('speacial')
          prof.save()
          return render(request, 'editprofile.html')
def sucess(request):
     sucess = 10
     return render(request, 'cart.html' ,{'sucess':sucess})     

def edit_item(request):
     rest_id = int(request.session['res_id'])

     rest  = Newsignup.objects.get(pk=rest_id)
     items = food_items.objects.filter(restaurent=rest_id)

     if request.method == "POST":
          id = request.POST.get('id')

          category = request.POST.get('Catagory').strip()
          foodname = request.POST.get('food_name')

          price = request.POST.get('price')
          itemdetail = request.POST.get('ingredentes')

          
  
  
          item = food_items.objects.get(pk=int(id))
          item.food_name = foodname
          item.item_price = price
          item.category = category
          item.item_ingredents = itemdetail
          item.save()
          
          
     

     


     return render(request, 'editmenu.html' ,{'rest_id' : rest_id,'items': items, 'res_owner': rest})     

def remove_menu(request):
     rest_id = int(request.session['res_id'])

     rest  = Newsignup.objects.get(pk=rest_id)
     items = food_items.objects.filter(restaurent=rest_id)

     if request.method == "POST":
          id = request.POST.get('id')
          ids = int(id)
          item = food_items.objects.get(pk=ids)
          print("delete",item)
          item.delete()
          
      
          print('deleteditem',item)
     return render(request, 'removeitem.html' ,{'rest_id' : rest_id,'items': items, 'res_owner': rest})   

     



def addcatageory(request):
     if request.method == "POST":

          
          cat= Add_catageory()
          cat.catageory= request.POST.get('catageory')   
          cat.save()    
          return render(request, 'catagory.html')


def add_to_cart(request):

     print(">>>>>> ", request.POST)
     uemail = str(request.session["email"])
     user = Users.objects.get(email=uemail)

     print("USER: ", request.session["email"] , user.username)
     
     if request.method == "POST":
          item_id = request.POST.get('item_id')
          quantity = request.POST.get('quantity')
  
          item = food_items.objects.get(id=item_id)

          rest_id = item.restaurent.id
          
          cust_orders  = get_cust_orders(request.session)
          user = Users.objects.get(pk=request.session['user_id'])
          orders = CartItem.objects.filter(ordered_by=user, order_date__date=datetime.now().date(),added_to_cart=False)

          for order in orders:
               if order.item.restaurent.id != rest_id:
                    order.delete()

          cartItems = CartItem()
          cartItems.item = item
          cartItems.quantity = quantity
          cartItems.ordered_by = user
          cartItems.save()
     
          return redirect('order', rest_id=rest_id)
def cart(request):
     # item = food_items.objects.get(id=item_id)

     # rest_id = item.restaurent.id
     uemail = str(request.session["email"])
     user = Users.objects.get(email=uemail)

     items = CartItem.objects.filter(order_date__date=datetime.now().date(), ordered_by= user, added_to_cart=False) 
     print("SUM::: ", sum([int(item.item.item_price) * int(item.quantity) for item in items]))
     print(">>>>>>",items)   
     print()
     total=0
    
    
     for itemss in items:
     
          subtotal = int(itemss.item.item_price) * int(itemss.quantity)
          print( type(subtotal))
          print('>>>>>>>>>>>>>>>>>',subtotal)
         
          total += subtotal
          print(total)
     return render(request, 'cart.html' ,{'item':items, 'total':total,'user':user})     

def orders(request):
     uemail = str(request.session["email"])
     user_mail = Users.objects.get(email=uemail)
     address_user = user_mail.address
     print("hello", address_user)
     address_ = Users.objects.filter(address = address_user)
     print(address_)

     items = CartItem.objects.filter(ordered_by= user_mail, order_date__date=datetime.now().date(), added_to_cart=False)
      # print("SUM::: ", sum([item.item.item_price * item.quantity for item in items]))
     totals=sum([int(item.item.item_price) * int(item.quantity) for item in items])


     if request.method == "POST":
          cart = Cart()
          cart.user = user_mail
          cart.grand_total = totals
          cart.address = address_user
          cart.save()
          
          items_saved = set()
          for item in items:
               
               if item.item.food_name not in items_saved:
                    cart.items_all.add(item)
                    items_saved.add(item.item.food_name)
               item.added_to_cart = True
               item.save()
               
               
          
          # cart.grand_total = request.POST.get('grand_total')
          return render(request, 'Ordersucessful.html',{ 'user':user_mail} ) 



     # item_obj = Cart()
     # item_obj.item = item
     # item_obj.user = user
     
def myOrders(request):
     uemail = str(request.session["email"])
     user_mail = Users.objects.get(email=uemail)

     orders = Cart.objects.filter( user = user_mail) 
     for item in orders:
          print('>>>>>>>lllllll',item.grand_total)
          print('>>>>items',item.items_all.all())
          print('orderby',item.items_all)
         
          
     return render(request, 'myorders.html',{'orders': orders, 'user':user_mail} ) 


def remove_item(request):
     uemail = str(request.session["email"])
     user_mail = Users.objects.get(email=uemail)
     # rest_id = int(request.session['res_id'])
     # rest  = Newsignup.objects.get(pk=rest_id)

     if request.method == "POST":
          id =  request.POST.get('id')
          ids = int(id)
          item = CartItem.objects.get(pk=ids)
          print("delete",item)
          item.delete()
      
          print('deleteditem',item)
     return redirect('cart')   


def logout(request):
     request.session.clear()    
     return render(request, 'index.html')

def api():
     result = requests.get()





























