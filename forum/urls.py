from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),
    path('create/', views.TopicCreateView.as_view(), name='topic_create'),
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('<int:pk>/delete/', views.TopicDeleteView.as_view(), name='topic_delete'),
    path('<int:pk>/reply/', views.PostCreateView.as_view(), name='post_create'),
]
