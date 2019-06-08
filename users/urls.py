from django.urls import path, include

from .views import UserView

urlpatterns = [
    path('me/', UserView.as_view(), name='user'),
]