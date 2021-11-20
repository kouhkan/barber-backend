from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_("Firstname"),
                                  max_length=128,
                                  null=True)
    last_name = models.CharField(_("Lastname"),
                                 max_length=128,
                                 null=False)
    username = models.CharField(_("Phone Number"),
                                max_length=11,
                                unique=True,
                                primary_key=True,
                                db_index=True)
    is_active = models.BooleanField(_("Active Status"),
                                    default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-date_joined',)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='user_profile')
    created = models.DateTimeField(_("Created"),
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated"),
                                   auto_now=True)
    status = models.BooleanField(_("Status"),
                                 default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('-created',)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
