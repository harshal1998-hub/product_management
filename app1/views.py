from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import orderform

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def order_form(request):
    if request.POST:
        obj = orderform()
        obj.customer = request.POST['customer']
        obj.product = request.POST['product']
        obj.price = request.POST['price']
        obj.Qty = request.POST['Qty']
        obj.total_price = request.POST['total_price']
        obj.save()
        return redirect('show_info')

    return render(request,'order_form.html')

def show_order(request):
    data = orderform.objects.all()
    return render(request,'order_show.html',{'data':data})

def update_order(request,id):
    obj = orderform.objects.get(id=id)
    if request.POST:
        obj.customer = request.POST['customer']
        obj.product = request.POST['product']
        obj.price = request.POST['price']
        obj.Qty = request.POST['Qty']
        obj.total_price = request.POST['total_price']
        obj.save()
        return redirect('show_info')

    return render(request,'order_form.html',{'data':obj})

def delete_order(request,id):
    obj = orderform.objects.get(id=id)
    obj.delete()
    return redirect('show_info')


