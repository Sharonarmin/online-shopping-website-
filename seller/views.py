from django.shortcuts import render
from seller.models import *
from buyer.models import *
from Admin.models import *
import datetime

# Create your views here.

def register(request):
    return render(request, 'sellerRegister.html')

def registerAction(request):
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
        return render(request, 'sellerRegister.html', {'msg':"username already exist"})
    else:
        user=register_tb1(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password,status='pending')
        user.save()
        return render(request, 'sellerRegister.html', {'msg':"registration successfull"})

def addProduct(request):
    user=catagory_tb.objects.all()
    return render(request, 'addProduct.html', {'data':user})

def addProductAction(request):
    pic =''
    if (len(request.FILES)>0):
        pic=request.FILES['fileUpload']
    else:
        pic = 'no pic'
    product=request.POST['product']
    details=request.POST['details']
    catagory=request.POST['catagory']
    catagory_obj=catagory_tb.objects.get(id=catagory)
    stock=request.POST['stock']
    price=request.POST['price']
    seller_id=request.session['seller_id']
    seller_obj=register_tb1.objects.get(id=seller_id)
    user=product_tb(seller=seller_obj,product=product,details=details,catagory=catagory_obj,stock=stock,price=price,file=pic)
    user.save()
    catagories=catagory_tb.objects.all()
    return render(request, 'addProduct.html', {'msg':"product added", 'data':catagories})

def myProducts(request):
    user=product_tb.objects.filter(seller=request.session['seller_id'])
    return render(request, 'myProducts.html', {'data':user})
def delete(request, uid):
    user=product_tb.objects.filter(id=uid).delete()
    user=product_tb.objects.all()
    return render(request, 'myProducts.html', {'data':user})

def update(request, uid):
    products=product_tb.objects.filter(id=uid)
    catagories=catagory_tb.objects.all()
    return render(request, 'update.html', {'data':products, 'catagory':catagories})
def updateAction(request):
    pic=' '
    
    
    productname=request.POST['product']
    details=request.POST['details']
    catagory=request.POST['catagory']
    stock=request.POST['stock']
    price=request.POST['price']
    uid =request.POST['uid']
    catagory_obj=catagory_tb.objects.get(id=catagory)
        
    product=product_tb.objects.get(id=uid)
    if (len(request.FILES)>0):
        pic=request.FILES['fileUpdate']
    else:
        pic=product.file
    product.product=productname
    product.details=details
    product.catagory=catagory_obj
    product.stock=stock
    product.price=price
    product.file=pic
    product.save()
    products=product_tb.objects.filter(seller=request.session['seller_id'])
    return render(request, 'myProducts.html', {'msg':"product updated", 'data':products})
    
def viewOrders(request):
    orders=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request, 'myOrders.html', {'data':orders})

def approveOrder(request, uid):
    user=order_tb.objects.filter(id=uid)
    user.update(status = 'approved')
    user=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request, 'myOrders.html' , {'data':user})

def denyOrder(request, uid):
    user=order_tb.objects.filter(id=uid)
    user.update(status = 'denied')
    user=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request, 'myOrders.html',{'data':user})
def cancelVerification(request, uid):
    order=order_tb.objects.filter(id=uid)
    order.update(status='Cancel verified')
    
    quantityNum=int(order[0].quantity)
    product=product_tb.objects.filter(id =order[0].product_id)
    product.update(stock= int(product[0].stock) + quantityNum)
    user=order_tb.objects.filter(seller_id=request.session['seller_id'])   
    return render(request, 'myorders.html', {'data':user})


def updateSellerProfile(request):
    user_id=request.session['seller_id']
    user=register_tb1.objects.filter(id=user_id)
    return render(request, 'updateSellerProfile.html',{'data':user})

def updateSellerProfileAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    uid=request.POST['uid']
    user=register_tb1.objects.filter(id=uid)
    user.update(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password)
    return render(request, 'homeSeller.html', {'data':user, 'msg':"Account updated"})

def trackingDetailsPage(request, uid):
    track=order_tb.objects.filter(id=uid)
    return render(request, 'trackingDetails.html', {'data':track})
    
        
def trackingDetailsfun(request):
    product=request.POST['uid']
    product_obj=order_tb.objects.get(id=product)
    place=request.POST['place']
    track=trackingDetails(product=product_obj,place=place,date=datetime.date.today(),time=datetime.datetime.now().strftime("%H:%M"))
    track.save()
    
    if 'delivered' in place:
        product_obj.status='delivered'
        product_obj.save()
    track=order_tb.objects.filter(id=product)
    return render(request,'trackingDetails.html',{'data':track})
    
    

