from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UnScientific.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^parking/$','Parking.views.index',name='index'),
    url(r'^parking/servicos/$','Parking.views.servicos',name='servicos'),
    url(r'^parking/localizacao/$','Parking.views.localizacao',name='localizacao'),
    url(r'^parking/quemsomos/$','Parking.views.quemsomos',name='quemsomos'),
    url(r'^parking/faleconosco/$','Parking.views.faleconosco',name='faleconosco'),
    )