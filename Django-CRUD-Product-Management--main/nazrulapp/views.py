from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def homePage(req):

    return render(req,'pages/home.html')

def productPage(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        price = float(req.POST.get('price'))
        quantity = float(req.POST.get('quantity'))
        dis_per = float(req.POST.get('dis_per'))
        tax = float(req.POST.get('tax'))
        image = req.FILES.get('image')

        sub_total = price*quantity
        dis = sub_total*(dis_per/100)
        tax = (sub_total-dis)*(tax/100)
        total = sub_total-dis+tax
        final_price = sub_total-(dis+tax)

        Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,

            dis_per=dis_per,
            tax=tax,
            total=total,
            final_price=final_price,
            image=image
         )

        messages.success(req,'Product Added Successfully')
        return redirect('product')
        
    data = Product.objects.all()
    context = {
        'products':data
    }

        
    return render(req,'pages/product.html',context)

def productEditPage(req,id):
    data = Product.objects.get(id=id)
    if req.method == 'POST':
        name = req.POST.get('name')
        price = float(req.POST.get('price'))
        quantity = float(req.POST.get('quantity'))
        dis_per = float(req.POST.get('dis_per'))
        tax = float(req.POST.get('tax'))
        image = req.FILES.get('image')

        sub_total = price*quantity
        dis = sub_total*(dis_per/100)
        tax = (sub_total-dis)*(tax/100)
        total = sub_total-dis+tax
        final_price = sub_total-(dis+tax)

         
        data.name=name
        data.price=price
        data.quantity=quantity

        data.dis_per=dis_per
        data.tax=tax
        data.total=total
        data.final_price=final_price
        data.image=image
         

        messages.success(req,'Product Edited Successfully')
        return redirect('product')
        
    
    context = {
        'product':data
    }

        
    return render(req,'pages/product.html',context)

def productDeletePage(req,id):
    Product.objects.filter(id=id).delete()
    return redirect('product')