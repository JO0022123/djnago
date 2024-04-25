from django.shortcuts import render,redirect
from .models import *
from .form import detailsform
# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'cat/index.html')
def reg(request):
    return render(request,'acc/reg.html')
def login(request):
    return render(request,'acc/login.html') 
def retrieve(request):
    details=company.objects.all()
    return render(request,'curd/show.html',{'details':details})
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=company.objects.create(name=name,age=age,address=address)
        obj.save()
        return redirect('retrieve/')
    else:
        return render(request,'curd/index1.html')
def delete(request,pk):
    c=company.objects.filter(id=pk)
    c.delete()
    return redirect('retrieve')

def edit(request,id):
    object=company.objects.get(id=id)
    return render(request,'curd/edit.html',{'object':object})

def update(request,id):
    object=company.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=company.objects.all()
        return redirect('retrieve')
    return render(request,'curd/edit.html',{'object':object})
def product(request):
    products=Product.objects.all()
    return render(request,'curd/card.html',{'products':products})