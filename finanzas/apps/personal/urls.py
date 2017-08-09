from django.conf.urls import include, url
from .views import(personal_create_view, personal_read_view, personal_update_view, personal_delete_view)

urlpatterns = [
    url(r'^crear/$', personal_create_view, name='crear'),
    url(r'^ver/$', personal_read_view, name='ver'),
    url(r'^editar/$', personal_update_view, name='editar'),
    url(r'^borrar/$', personal_delete_view, name='borrar'),
]
