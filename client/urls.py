# noinspection PyUnresolvedReferences
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('client/', views.client_view, name = "client"),
    path('course/', views.course_view, name = "courses"),
    path('ajoutc/', views.ajout_view, name = "ajoutCli"),
    path('client/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('client/<int:client_id>/modify/', views.client_modify, name='client_modify'),
    path('search/', views.search_client, name='recherche'),
]