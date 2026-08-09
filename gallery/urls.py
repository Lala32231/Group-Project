from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='list'),
    path('create/', views.AlbumCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('<int:pk>/add-photo/', views.PhotoCreateView.as_view(), name='add_photo'),
    path('<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='delete'),
]
