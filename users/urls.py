from django.urls import path, include
from .views import home, 
urlpatterns = [
    path('', home, name='users-home'),
    path('profile/', profile, name='users-profile'),
]
