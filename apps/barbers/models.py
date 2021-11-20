from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import User


class Barber(models.Model):
    barber = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='barber_user')
    shop_name = models.CharField(_("Shop Name"),
                                 max_length=128,
                                 null=False)
    province = models.CharField(_("Province"),
                                max_length=128,
                                null=True,
                                blank=True)
    city = models.CharField(_("City"),
                            max_length=128,
                            null=True,
                            blank=True)
    address = models.TextField(_("Shop Address"))
    location = models.CharField(_("Map Location"),
                                max_length=512,
                                null=True,
                                blank=True)
    start_time = models.CharField(_("Start Time"),
                                  max_length=5,
                                  null=True,
                                  blank=True)
    end_time = models.CharField(_("End Time"),
                                max_length=5,
                                null=True,
                                blank=True)
    cover = models.ImageField(_("Cover"),
                              upload_to='barber/',
                              null=True,
                              blank=True)
    inner_1 = models.ImageField(_("Inner Picture"),
                                upload_to='barber/',
                                null=True,
                                blank=True)
    inner_2 = models.ImageField(_("Inner Picture"),
                                upload_to='barber/',
                                null=True,
                                blank=True)
    inner_3 = models.ImageField(_("Inner Picture"),
                                upload_to='barber/',
                                null=True,
                                blank=True)
    description = models.TextField(_("Description"),
                                   null=True,
                                   blank=True)
    created = models.DateTimeField(_("Created BarberShop"),
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated Data"),
                                   auto_now=True)
    status = models.BooleanField(_("Status"),
                                 default=False)

    def __str__(self):
        return f'{self.shop_name}'

    class Meta:
        ordering = ('-created',)


class Service(models.Model):
    barber = models.ForeignKey(Barber,
                               on_delete=models.CASCADE,
                               related_name='barber_service')
    service_name = models.CharField(_("Service Name"),
                                    max_length=128)
    amount = models.PositiveIntegerField(_("Amount"))
    created = models.DateTimeField(_("Created"),
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated Data"),
                                   auto_now=True)
    status = models.BooleanField(_("Status"),
                                 default=True)

    def __str__(self):
        return f'{self.service_name}'

    class Meta:
        ordering = ('-created', )
