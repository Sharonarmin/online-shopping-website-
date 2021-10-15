from django.shortcuts import render, redirect
from Admin.models import *
from seller.models import *
from buyer.models import *


# Create your views here.

def index(request):
    if 'buyer_id' in request.session:
        product=product_tb.objects.all().order_by('-id')[:10]
        return render(request, 'home.html',{"data":product})
    elif 'seller_id' in request.session:
        orders=order_tb.objects.filter(seller_id=request.session['seller_id'])
        return render(request, 'homeSeller.html',{'data':orders})
    elif 'admin_id' in request.session:
        return render(request, 'adminhome.html')
    else:
        product=product_tb.objects.all().order_by('-id')[:10]
        return render(request, 'index.html',{'data':product})

def login(request):
    return render(request, 'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(username=username,password=password)
    if (user.count()>0):
        request.session['buyer_id']=user[0].id
        return redirect('index')
    else:
        user=register_tb1.objects.filter(username=username,password=password)
        if (user.count()>0):
            if user[0].status == 'approved':
                request.session['seller_id']=user[0].id
                return render(request, 'homeSeller.html', {"data":user})
            else:
                return render(request, 'login.html', {'msg':"not approved"})
        else:
            user=admin_tb.objects.filter(username=username, password=password)
            if (user.count()>0):
                request.session['admin_id']=user[0].id
                return render(request, 'adminhome.html',{"data":user})
            else:
                return render(request, 'login.html', {'msg':"incorrect password or username"})

def catagory(request):
    return render(request, 'catagory.html')

def catagoryAction(request):
    catagory =request.POST['catagory']
    catagory=catagory_tb(catagory=catagory)
    catagory.save()
    return render(request, 'catagory.html', {"msg":"catagory added sucessfully"})
    
def ViewSellers(request):
    user = register_tb1.objects.all()
    return render(request, 'ViewSellers.html', {"data":user})

def approve(request,uid):
    user=register_tb1.objects.filter(id=uid)
    user.update(status='approved')
    user = register_tb1.objects.all()
    return render(request, 'ViewSellers.html', {'data':user})
def deny(request,uid):
    user=register_tb1.objects.filter(id=uid)
    user.update(status='denied')
    user=register_tb1.objects.all()
    return render(request, 'ViewSellers.html', {'data':user})

def deleteUser(request, uid):
    user=register_tb1.objects.filter(id=uid).delete()
    user=register_tb1.objects.all()
    return render(request, 'ViewSellers.html', {'data':user})

def forgotPassword(request):
    return render(request, 'forgotPassword.html')

def forgotPasswordAction(request):
    username=request.POST['username']
    user=register_tb.objects.filter(username=username)
    if (user.count() > 0 ):
        return render(request,'buyerRecoveryPassword.html', {'data':user[0].username})
    else:
        user=register_tb1.objects.filter(username=username)
        if (user.count() > 0):
            return render(request, 'sellerRecoveryPassword.html', {'data':user[0].username})
        else:
            user=admin_tb.objects.filter(username=username)
            if (user.count() > 0):
                return render(request, 'adminRecoveryPassword.html', {'data':user[0].username})
            else:
                return render(request, 'forgotPassword.html', {'msg':"Incorrect username"})

def buyerRecoveryPasswordAction(request):
    address=request.POST['address']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    user=register_tb.objects.filter(address=address,phone=phone,country=country,username=username)
    if (user.count() > 0):
        return render(request,'buyerChangePassword.html',{'data':user[0].username})
    else:
        return render(request, 'forgotPassword.html', {'msg':"incorrect details"})
    
def sellerRecoveryPasswordAction(request):
    address=request.POST['address']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    user=register_tb1.objects.filter(address=address,phone=phone,country=country,username=username)
    if (user.count() > 0):
        return render(request, 'sellerChangePassword.html', {'data':user[0].username})
    else:
         return render(request, 'forgotPassword.html', {'msg':"incorrect details"})

def adminRecoveryPasswordAction(request):
    username=request.POST['username']
    password=request.POST['password']
    Confirmpassword=request.POST['ConfirmPassword']
    if password == Confirmpassword:
        user=admin_tb.objects.filter(username=username)
        user.update(password=password)
        return render(request, 'login.html')
    else:
        return render(request, 'adminRecoveryPassword.html', {'msg':"Password entered not matching"})

def buyerChangePasswordAction(request):
    username=request.POST['username']
    password=request.POST['password']
    ChangePassword=request.POST['ChangePassword']
    if password == ChangePassword:
        user=register_tb.objects.filter(username=username)
        user.update(password=password)
        return render (request, 'login.html')
    else:
        user=register_tb.objects.filter(username=username)
        return render(request,'buyerChangePassword.html', {'msg':"Password entered not matching",'data':user[0].username})

def sellerChangePasswordAction(request):
    username=request.POST['username']
    password=request.POST['password']
    ChangePassword=request.POST['ChangePassword']
    if password == ChangePassword:
        user=register_tb1.objects.filter(username=username)
        user.update(password=password)
        return render(request, 'login.html')
    else:
         user=register_tb1.objects.filter(username=username)
         return render(request,'sellerChangePassword.html', {'msg':"Password entered not matching",'data':user[0].username})
        
    

def logOut(request):
    if 'buyer_id' in request.session:
        del request.session['buyer_id']
    if 'seller_id' in request.session:
        del request.session['seller_id']
    if 'admin_id' in request.session:
        del request.session['admin_id']
    return render(request,'index.html') 
