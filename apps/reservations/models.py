from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import User
from apps.barbers.models import Barber, Service


class Reserve(models.Model):
    STATUS = (
        ('r', 'Reserved'),
        ('a', 'Another Person'),
        ('c', 'Canceled'),
        ('f', 'Free'),
        ('w', 'Waiting')
    )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_reserve')
    barber = models.ForeignKey(Barber,
                               on_delete=models.CASCADE,
                               related_name='barber_reserve')
    time = models.CharField(_("Reserve Time"),
                            max_length=5)
    date = models.DateField(_("Date"))
    services = models.ManyToManyField(Service)
    created = models.DateTimeField(_('Created'),
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated"),
                                   auto_now=True)
    status = models.CharField(_('Status'),
                              max_length=1,
                              choices=STATUS,
                              default='w')

    def __str__(self):
        return f'{self.user.full_name}'

    class Meta:
        ordering = ('-created', )