from django.urls import path, include
from .views import home, profile, RegisterView, create_group, add_group, my_groups, team, chat, callendar

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('create_group/', create_group, name='create_group'),
    path('add_group/', add_group, name='add_group'),
    path('my_groups/', my_groups, name='my_groups'),
    path('team/', team, name='team'),
    path('chat/', chat, name='chat'),
    path('callendar/', callendar, name='callendar'),
]
