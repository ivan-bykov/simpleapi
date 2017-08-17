from django.conf.urls import url

from . import views

urlpatterns = \
    [
    url(r'^$', views.index, name='index'),
    url(r'^state/$', views.state, name='state'),
    url(r'^api/uploadText/$', views.uploadText, name='uploadText'),
    url(r'^api/getText/$', views.getText, name='getText'),
    ]
