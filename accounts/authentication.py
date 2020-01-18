from accounts.models import User, Token
import sys

class PasswordlessAuthenticationBackend(object):
    def authenticate(self, uid):
        print('authenticate called',file=sys.stderr)
        try:
            token = Token.objects.get(uid=uid)
            #print(f'token get, uid = {token.uid}, email = {token.email}',file=sys.stderr)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            #print('user not not exist',file=sys.stderr)
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            #print('token not not exist',file=sys.stderr)
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
