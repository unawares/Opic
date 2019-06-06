from .models import CustomUser
from rest_framework import viewsets
from .serializers import UserSerializer


# TODO: UserViewSet shows list of user. Remove it.
# User must see only its own profile, not others

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
