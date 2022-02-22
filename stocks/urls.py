from django.urls import path
from stocks import views


app_name = 'stocks'

urlpatterns = [
    path('', views.produse_view.as_view(), name= 'produse'),
    path('pungi/', views.pungi_view.as_view(), name='pungi'),
    path('folie/', views.folie_view.as_view(), name='folie'),
    path('pungiview/', views.PungiView.as_view(), name= 'pungiview'),
    path('folieview/', views.FolieView.as_view(), name= 'folieview'),
    path('modifica-pungi/<int:pk>/', views.UpdatePungiView.as_view(), name= 'modifica-pungi'),
    path('modifica-folie/<int:pk>/', views.UpdateFolieView.as_view(), name= 'modifica-folie'),
    path('sterge-pungi/<int:pk>/', views.deactivate_Pungi, name= 'sterge-pungi'),
    path('sterge-folie/<int:pk>/', views.deactivate_Folie, name= 'sterge-folie'),
    path('comenzi/', views.ComenziView, name= 'comenzi'),

]