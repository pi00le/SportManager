from django.urls import path, include
from .views import home, profile, RegisterView, create_group, add_group

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('create_group/', create_group, name='create_group'),
    path('add_group/', add_group, name='add_group'),
]
