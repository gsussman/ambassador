from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^howitworks/$', views.hiw, name='hiw'),
    url(r'^signup/$', views.signup, name='signup'),
]