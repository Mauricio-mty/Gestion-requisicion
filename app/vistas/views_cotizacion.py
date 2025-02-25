from django.shortcuts import render,get_object_or_404,redirect
from  app.models import Cotizacion

def list_Cotizacion(request):
    tipo=Cotizacion.objects.all()
    return render(request)#request,'path .html',{tipo:tipo}

def oneCotizacion(request,id):
    tipo=get_object_or_404(Cotizacion,pd=id)
    return render(request)

def new_cotizacion(request):
    data=Cotizacion( 
        idcotizacion=request.POST[''],
        fechacotización=request.POST[''],
        fechaentrega=request.POST[''],
        precio=request.POST[''],
        idrequisicion=request.POST[''],
        idproveedor=request.POST['']
    )

def delete_cotizacion(request_id):
    data=  Cotizacion.objects.get(idcotizacion=request_id)
    data.delete()  
    print(request_id)
    return redirect('/app/')

