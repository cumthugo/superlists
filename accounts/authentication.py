from accounts.models import MyUser, Token
import sys

class PasswordlessAuthenticationBackend:
    def authenticate(self, request, uid): #request param must be present
        try:
            token = Token.objects.get(uid=uid)
            return MyUser.objects.get(email=token.email)
        except MyUser.DoesNotExist:
            return MyUser.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            return None
