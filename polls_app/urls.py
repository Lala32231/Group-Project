from django.urls import path
from . import views

app_name = 'polls_app'

urlpatterns = [
    path('', views.PollListView.as_view(), name='list'),
    path('create/', views.PollCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PollDetailView.as_view(), name='detail'),
    path('<int:pk>/vote/', views.PollVoteView.as_view(), name='vote'),
    path('<int:pk>/delete/', views.PollDeleteView.as_view(), name='delete'),
]
