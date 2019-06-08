from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import authentication, permissions
# TODO: UserViewSet shows list of user. Remove it.
# User must see only its own profile, not others


class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response("hello")

    def put(self):
        pass

    @classmethod
    def get_extra_actions(cls):
        return []
