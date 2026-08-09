from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile_detail'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/role/', views.RoleChangeView.as_view(), name='role_change'),
]
