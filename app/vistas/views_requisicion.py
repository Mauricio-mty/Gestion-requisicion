from django.shortcuts import render,get_object_or_404,redirect
from  app.models import Requisicion

def list_Requisicion(request):
    tipo=Requisicion.objects.all()#.order_by('campo') '-campo':ordena de forma descendente
    return render(request)#request,'path .html',{tipo:tipo}

def oneRequisicion(request,id):
    tipo=get_object_or_404(Requisicion,pd=id)
    return render(request)

def new_Requisicion(request):
    data=Requisicion(
        idrequisicion=request.POST['idrequisicon'],
        numeroserie=request.POST['numeroserie'],
       fechageneracion=request.POST['fechageneracion'],
       fechaentrega =request.POST['fechaentrega'],
       estado=request.POST['estado'],
       idempleado=request.POST['idempleado']
    )
    data.save()
    return redirect('/app/')

def delete(requisicion_id):
    data=Requisicion.objects.get(idrequisicion=requisicion_id)
    data.delete()
    print(requisicion_id)
    return redirect('/app/')