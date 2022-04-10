from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def jwt_encode(user):
    refresh = TokenObtainPairSerializer.get_token(user)
    return refresh.access_token, refresh
