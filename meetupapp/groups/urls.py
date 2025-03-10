from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('create/', views.create_group, name='create_group'),
    path('search/', views.search_groups, name='search_groups'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:group_id>/join/', views.join_group, name='join_group'),
    path('<int:group_id>/edit/', views.edit_group, name='edit_group'),
    path('<int:group_id>/delete/', views.delete_group, name='delete_group'),
]
