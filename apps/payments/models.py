from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.reservations.models import Reserve


class Payment(models.Model):
    STATUS = (
        ('c', 'Canceled'),
        ('p', 'Paid'),
        ('n', 'Not Paid')
    )
    reserve = models.ForeignKey(Reserve,
                                on_delete=models.CASCADE,
                                related_name='reserve_payment')
    code = models.CharField(_("Paid Code"),
                            max_length=512)
    authority = models.CharField(_("Authority Code"),
                                 max_length=512)
    amount = models.PositiveIntegerField(_("Amount"))
    created = models.DateTimeField(_('Created'),
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated"),
                                   auto_now=True)
    status = models.CharField(_('Status'),
                              max_length=1,
                              choices=STATUS,
                              default='n')

    def __str__(self):
        return f'{self.reserve.user.full_name}'

    class Meta:
        ordering = ('-created', )