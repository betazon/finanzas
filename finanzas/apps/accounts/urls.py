from django.conf.urls import include, url
from .views import(login_view, profile_view, change_pass_view, reset_pass_view, logout_view)

urlpatterns = [
    url(r'^$', login_view, name='login'),
    url(r'^profile/', profile_view, name='profile'),
    url(r'^change_pass/', change_pass_view, name='change_pass'),
    url(r'^reset_pass/', reset_pass_view, name='reset_pass'),
    url(r'^logout/', logout_view, name='logout'),
]
