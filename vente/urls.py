from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path('client/', views.client_view, name="client"),
    path('course/',views.course_view, name = "courses"),
    path('vente/', views.vente_view, name = "vente"),
    path('ajoutVente/',views.ajoutVente_view, name = "ajoutVente"),
    path('vente/<int:vente_id>/delete/', views.vente_delete, name='vente_delete'),
    path('vente/<int:id>/modify/', views.vente_modify, name='vente_modify'),
]