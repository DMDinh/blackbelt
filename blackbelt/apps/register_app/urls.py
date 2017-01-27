from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^quotes$', views.success),
    url(r'^logout$', views.logout),
    url(r'^submit$', views.submit),
    url(r'^add', views.favorite),
    url(r'^users', views.users),
    # url(r'^(?P<id>\d+)/favorite$', views.favorite),
]
