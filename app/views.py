from django.urls import path
#import sys
#import os 
#sys.path.append(os.path.abspath('vistas'))
from app.vistas import views_areaEmpleado, views_empleado




urlpatterns=[
    #iran todos los path que se utilicen
    path('',views_areaEmpleado.list_areaEmpleado),
    path('area/',views_areaEmpleado.new_area,name='create_area'),
    path('delete_area/<int:area_id>/',views_areaEmpleado.delete,name='delet_area')
    #path('update_area/<int:area_id>/',views_areaEmpleado.update,name='update_area')

]



