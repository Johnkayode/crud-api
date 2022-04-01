from django.db import models

from django.utils.translation import gettext_lazy as _

class Customer(models.Model):

    first_name = models.CharField(_("first name"), blank=False, null=False, max_length=250)
    last_name = models.CharField(_("last name"), blank=False, null=False, max_length=250)
    email = models.CharField(_("email"), blank=False, null=False, max_length=250, unique=True)
    city = models.CharField(_("city"), blank=False, null=False, max_length=250
    )
    state = models.CharField(_("state"), blank=False, null=False, max_length=250
    )
    phone_number = models.CharField(
        _("phone number"), blank=False, null=False, max_length=11
    )
    

    def __str__(self):
        return self.email
