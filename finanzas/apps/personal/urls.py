from django.conf.urls import include, url
from .views import(personal_create_view, personal_list_view, personal_update_view, personal_delete_view, personal_cargartxt_view)

urlpatterns = [
    url(r'^crear/$', personal_create_view, name='crear'),
    url(r'^listar/$', personal_list_view, name='listar'),
    url(r'^editar/(?P<persona_id>[0-9]+)/', personal_update_view, name='editar'),
    url(r'^borrar/$', personal_delete_view, name='borrar'),
    url(r'^cargar_txt/$', personal_cargartxt_view, name='cargartxt'),

]
