from django.shortcuts import render,get_object_or_404,redirect
from  app.models import Empleado


def list_Empleado(request):
    tipo=Empleado.objects.all()
    return render(request)#request,'path .html',{tipo:tipo}

def new_Empleado(request):
    data=Empleado.objects.get(
            idempleado=request.POST['idempleado'],
            nombreempleado=request.POST['idempleado'],
            contrasena=request.POST['contrasena'],
            idarea=request.POST['idarea'],
            idtipoempleado=request.POST['idtipoempleado']
                              )
    data.save()
    return redirect('/app/')

def delete(request,number_id):
    data=Empleado.objects.get(idempleado=number_id)
    data.delete()
    print(number_id)
    return redirect('/app/')

#def update
#def retorn id


