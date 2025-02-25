from django.shortcuts import render,get_object_or_404,redirect
from  app.models import Proveedor

def list_Proveedor(request):
    tipo=Proveedor.objects.all()
    return render(request)#request,'path .html',{tipo:tipo}

def oneProveedor(request_id):
    data=Proveedor.objects.get(idproveedor=request_id)
    return redirect('/app/')

def new_Proveedor(request):
    data=Proveedor(
        idproveedor=request.POST[''],
        nombreproveedor=request.POST[''],
        direccion=request.POST[''],
        telefono=request.POST[''],
        nombrecontacto=request.POST[''],
        correo=request.POST[''],
        idtipoproveedor=request.POST['']
    )
    data.save()
    return redirect('/app/')

def delete_Proveedor(request_id):
    data=Proveedor.objects.get(idproveedor=request_id)
    data.delete() 
    return redirect('/app/')
