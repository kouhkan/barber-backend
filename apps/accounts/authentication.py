from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from apps.accounts.models import User


class UsernameBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return User
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
