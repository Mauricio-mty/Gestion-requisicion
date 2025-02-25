from django.shortcuts import render,get_object_or_404,redirect
from  app.models import productosRequisicion


def list_productosRequisicion(request):
    data=productosRequisicion.objects.all()
    return render(request)

def one_register(register_id):
    data=productosRequisicion.objects.get(idpropductosrequisicion=register_id)
    print(data)
    return redirect('/app/')
    


def new_register(request):
    data=productosRequisicion(
       idproductosrequisicion =request.POST['idproductorequi'],
        nombreproducto=request.POST['nombreproducto'],
        descripcion=request.POST['descripcion'],
        cantidad=request.POST['cantidad'],
        unidad=request.POST['unidad'],
        idrequisicion=request.POST['idrequisicion']
    )

    data.value()
    return redirect('/app/')

def delete_register(register_id):
    data=productosRequisicion.objects.get(idpropductosrequisicion=register_id)
    data.delete()
    print(register_id)
    return redirect('/app/')


#def update()