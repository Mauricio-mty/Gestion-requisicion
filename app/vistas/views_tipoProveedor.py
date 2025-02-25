from django.shortcuts import render,get_object_or_404,redirect
from  app.models import tipoProveedor

def list_tipoProveedor(request):
    tipo=tipoProveedor.objects.all()
    return render(request)#request,'path .html',{tipo:tipo}

def new_tipoProveedor(request):
    data=tipoProveedor( 
        idtipoproveedor=request.POST['idarea'],
        nombretipoproveedor=request.POST['nombrearea'])
    data.save()
    return redirect('/app/')

def delete(request,area_id):
    data=tipoProveedor.objects.get(idtipoproveedor=area_id)
    data.delete()
    print(area_id)
    return redirect('/app/')

def update(request,area_id):
    data=tipoProveedor.objects.get(idtipoproveedor=area_id)
    print(data)
    return redirect('/app/')