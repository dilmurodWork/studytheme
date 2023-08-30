from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('profile/<int:pk>', user_profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('register/', registration_user, name='register'),
    path('create-room', room_create, name='creat-room'),
    path('create-topic', create_topic, name='creat-topic'),
    path('room_detail/<int:pk>', room_detail, name='room'),
    path('update-room/<int:pk>', room_update, name='update-room'),
    path('delete-room/<int:pk>', room_delete, name='delete-room'),
    path('delete-message/<int:pk>', message_delete, name='delete-message'),
    path('edit-user', edit_user, name='edit-user'),
]
