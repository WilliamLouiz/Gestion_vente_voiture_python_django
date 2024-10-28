from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path('client/', views.client_view, name="client"),
    path('course/',views.course_view, name = "courses"),
    path('ajoutV/',views.ajoutv_view, name = "ajoutV"),
    path('voiture/<int:voiture_id>/delete/', views.voiture_delete, name='voiture_delete'),
    path('voiture/<int:voiture_id>/modify/', views.voiture_modify, name='voiture_modify'),
]