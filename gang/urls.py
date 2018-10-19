from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='landing'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^createhood/$', views.createhood, name='createhood'),
    url(r'^edithood/(\d+)$', views.edithood, name='edithood'),
    url(r'^deletehood/(\d+)$',views.delhood, name = 'deletehood'),
    url(r'^join/(\d+)',views.join, name = 'joinhood'),
]
