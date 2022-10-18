from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('kotxeak_add/', views.kotxeak_add, name='kotxeak_add'),
    path('kotxeak_add/kotxeak_addrecord/', views.kotxeak_addrecord, name='kotxeak_addrecord'),  #dirige el add.html a la funcion addrecord de views
    
    path('delete/<int:id>', views.delete, name='delete'),
    
    path('kotxea_update/<int:id>', views.kotxea_update, name='kotxea_update'),
    path('kotxea_update/kotxea_updaterecord/<int:id>', views.kotxea_updaterecord, name='kotxea_updaterecord'),  
    
    #petsona
    path('pertsona_add/', views.pertsona_add, name='pertsona_add'),
    path('pertsona_add/pertsona_addrecord/', views.pertsona_addrecord, name='pertsona_addrecord'),  #dirige el add.html a la funcion addrecord de views
    
    path('pertsona_add/pertsona_delete/<int:id>', views.pertsona_delete, name='pertsona_delete'),
    
    path('pertsona_add/pertsona_update/<int:id>', views.pertsona_update, name='kotxea_update'),
    path('pertsona_add/pertsona_update/pertsona_updaterecord/<int:id>', views.pertsona_updaterecord, name='pertsona_updaterecord'), 
]