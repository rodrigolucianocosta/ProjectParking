from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UnScientific.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^parking/$','Parking.views.index',name='index'),
    url(r'^parking/cadastracliente/$','Parking.views.CadastraCliente',name='clientes'),
    #url para cadastrar o cliente

    url(r'^parking/listacliente/$','Parking.views.ListaCliente',name='lista_clientes'),
    #url para listar os clientes

    url(r'^parking/alteracliente/(?P<codigo>[0-9+])/$','Parking.views.AlteraCliente',name='alteracliente'),
    #url para alterar os clientes
    
    #-------------------------------------------------------------------------------------------------------------------

    url(r'^parking/cadastraveiculo/$','Parking.views.CadastraVeiculo',name='cadastraVeiculo'),
    #url para cadastrar veiculos

    url(r'^parkinglistaveiculos/$','Parking.views.ListaVeiculos',name='lista_veiculos'),
    # url(r'^parking/alteraveiculo/$','Parking.views.Alteraveiculo',name='alteraveiculo')

    url(r'^parking/alteraveiculo(?P<codigo>[0-9])/$', 'Parking.views.Alteraveiculo',name='al'),


    #------------------------------------------------------------------------------------------------------------------


    url(r'^parking/cadastravaga/$','Parking.views.CadastraVaga',name='cadastravaga'),
    #url para cadastrar vagas
    
   
    #url(r'^parking/alteravaga/$','Parking.views.Alteravaga',name='alteravaga')
    
    )