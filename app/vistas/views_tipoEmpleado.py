from django.shortcuts import render,get_object_or_404,redirect
from  app.models import tipoEmpleado

def list_tipoEmpleapdo(request):
    tipo=tipoEmpleado.objects.all()
    return render(request,)#request,'path .html',{tipo:tipo}

def new_tipoEmpledo(request):
    data=tipoEmpleado(
        idtipoempleado=request.POST['idtipoempleado'],
        nombretipo=request.POST['nombretipo']
        )
    data.save()
    return redirect('/app/')

def delete(request,tipo_id):
    data=tipoEmpleado.objects.get(idtipoempleado=tipo_id)
    data.delete()
    return redirect('/app/')


#def update