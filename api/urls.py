from django.urls import path, include

urlpatterns = [
    path('users/', include('api.users.urls')),
    path('friends/', include('api.friends.urls'))
]