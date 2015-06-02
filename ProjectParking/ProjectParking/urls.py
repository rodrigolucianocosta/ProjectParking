from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UnScientific.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^parking/$','Parking.views.index',name='index'),
    url(r'^parking/cadastracliente/$','Parking.views.CadastraCliente',name='clientes'),
    url(r'^parking/cadastraveiculo/$','Parking.views.CadastraVeiculo',name='cadastraVeiculo'),
    url(r'^parking/cadastravaga/$','Parking.views.CadastraVaga',name='cadastravaga'),
    #url(r'^parking/alteracliente/(?P<codigo>[0-9+])/$','Parking.views.AlteraCliente',name='alteracliente'),
    url(r'^parking/alteracliente/$','Parking.views.Alteracliente',name='alteracliente')
   # url(r'^parking/alteraveiculo/$','Parking.views.Alteraveiculo',name='alteraveiculo')
    #url(r'^parking/alteravaga/$','Parking.views.Alteravaga',name='alteravaga')
    
    )