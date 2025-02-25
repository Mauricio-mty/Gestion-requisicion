from django.shortcuts import render,get_object_or_404,redirect
from  app.models import areaEmpleado

def list_areaEmpleado(request):
    tipo=areaEmpleado.objects.all()
    print(tipo)
    return render(request,'index.html',{"tipo":tipo})#request,'path .html',{tipo:tipo}

def one_areaEmpleado(request,area_id):
    data=areaEmpleado.objects.get(idarea=area_id)
    print(data)
    return redirect('/app/')


def new_area(request):
    data=areaEmpleado(idarea=request.POST['idarea'],nombrearea=request.POST['nombrearea'])
    data.save()
    return redirect('/app/')

def delete(request,area_id):
    data=areaEmpleado.objects.get(idarea=area_id)
    data.delete()
    print(area_id)
    return redirect('/app/')

def update(request,area_id):
    data=areaEmpleado.objects.get(idarea=area_id)
    print(data)
    return redirect('/app/')
