from django.conf.urls import include, url
from .views import(personal_create_view, personal_list_view, personal_update_view, personal_delete_view, personal_cargartxt_view)

urlpatterns = [
    url(r'^crear/$', personal_create_view, name='crear'),
    url(r'^listar/$', personal_list_view, name='listar'),
<<<<<<< HEAD
    url(r'^editar/(?P<idempleado>\d+)$', personal_update_view, name='editar'),
=======
    #url(r'^editar/$', personal_update_view, name='editar'),
    url(r'^editar/(?P<empleado_id>+)/$', personal_update_view, name='editar'),








>>>>>>> 916bf0cadf935175ceba5ea0f2ea5b1bd3f1cd6a
    url(r'^borrar/$', personal_delete_view, name='borrar'),




    url(r'^cargar_txt/$', personal_cargartxt_view, name='cargartxt'),

]
