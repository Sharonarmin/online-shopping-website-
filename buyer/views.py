from django.shortcuts import render
from buyer.models import *
from seller.models import *
from Admin.models import *
import datetime

# Create your views here.
def register1(request):
    return render(request, 'register1.html')

def registerAction1(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    user = register_tb.objects.filter(username=username)
    userSeller = register_tb1.objects.filter(username=username)
    userAdmin = admin_tb.objects.filter(username=username)
    if (user.count()>0 or userSeller.count()>0 or userAdmin.count()>0):
        return render(request, 'register1.html', {"msg":"username already exist"})
    else:  
        user=register_tb(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password)
        user.save()
        return render(request, 'register1.html', {'msg':"registration successfull"})

def productsAvailable(request):
    available=product_tb.objects.all()
    return render(request, 'productsAvailable.html', {'data':available})

def add_to_cart(request,uid):
    products =product_tb.objects.filter(id = uid)
    return render(request, 'add_to_cart.html', {'data':products})

def add_to_cart_action(request):
    product=request.POST['uid']
    product_obj=product_tb.objects.get(id=product)
    address=request.POST['address']
    contact=request.POST['contact']
    quantity=int(request.POST['quantity'])
    stock=int(product_obj.stock)
    total=request.POST['total']
    buyer=request.session['buyer_id']
    buyer_obj=register_tb.objects.get(id=buyer)
    seller=product_obj.seller
    if quantity > stock:
        return render(request,'add_to_cart.html', {'msg':"insufficient stock"})
    else:
        cart=add_to_cart_tb(product=product_obj,address=address,contact=contact,quantity=quantity,total=total,seller=seller,buyer=buyer_obj)
        cart.save()
        available=product_tb.objects.all()
        return render(request, 'productsAvailable.html', {'data':available})

def viewCart(request):
    cart=add_to_cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request, 'viewCart.html', {'data':cart})

def cartAction(request):
    products=request.POST.getlist('cartProducts')
    for i in products:
        cart=add_to_cart_tb.objects.filter(id=i)
        order=order_tb(product=cart[0].product,seller=cart[0].seller,address=cart[0].address,contact=cart[0].contact,quantity=cart[0].quantity,total=cart[0].total,buyer=cart[0].buyer,date=datetime.date.today())
        order.save()
        quantitynum=int(cart[0].quantity)
        stocknum=int(cart[0].product.stock)
        product=product_tb.objects.filter(id=cart[0].product_id)
        product.update(stock=stocknum-quantitynum)
        cart.delete()
    cart=add_to_cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request, 'viewCart.html', {'data':cart})

def ordered(request):
    ordered=order_tb.objects.all()
    return render(request, 'order.html', {'data':ordered})

def cancelOrder(request, uid):
    user=order_tb.objects.filter(id=uid)
    user.update(status = 'Canceled')
    user=order_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'order.html', {'data':user})

def deleteCart(request, uid):
    cart=add_to_cart_tb.objects.filter(id=uid)
    cart.delete()
    cart=add_to_cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewCart.html', {'data':cart})

def searchProduct(request):
    return render(request, 'searchProduct.html')
    
def productResults(request):
    result=request.GET.get('searchProduct')
    product=product_tb.objects.filter(product__contains=result)
    return render(request, 'productsAvailable.html', {'data':product})
    

def sortProducts(request):
    catagory=catagory_tb.objects.all()
    return render(request, 'sort.html', {'data':catagory})

def sortAction(request):
    price=int(request.GET.get('price'))
    catagory=request.GET.get('sort')
    product=product_tb.objects.filter(catagory=catagory, price__lte= price)
    return render(request, 'productsAvailable.html',{'data':product})

def updateBuyerProfile(request):
    user_id=request.session['buyer_id']
    user=register_tb.objects.filter(id=user_id)
    return render(request, 'updateBuyerProfile.html', {'data':user})

def updateProfileAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    uid=request.POST['uid']
    user=register_tb.objects.filter(id=uid)
    user.update(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password)
    return render(request, 'home.html', {'msg':"Profile updated",'data':user})

def buyerTrackingDetails(request,uid):
    user=trackingDetails.objects.filter(product=uid)
    return render(request, 'buyerTrackingDetails.html',{'data':user})
