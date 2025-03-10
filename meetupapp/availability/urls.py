from django.urls import path
from . import views

app_name = 'availability'
urlpatterns = [
    path('update/', views.update_availability, name='update_availability'),
    path('add_override/', views.add_override, name='add_override'),
]