# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Personne(models.Model):

    #__Personne_FIELDS__
    idpersonne = models.IntegerField(null=True, blank=True)
    nom_et_prenom = models.TextField(max_length=255, null=True, blank=True)
    grade = models.TextField(max_length=255, null=True, blank=True)
    date_naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    mle_solde = models.TextField(max_length=255, null=True, blank=True)
    photo = models.TextField(max_length=255, null=True, blank=True)
    corps_fk = models.ForeignKey(corps, on_delete=models.CASCADE)

    #__Personne_FIELDS__END

    class Meta:
        verbose_name        = _("Personne")
        verbose_name_plural = _("Personne")


class Corps(models.Model):

    #__Corps_FIELDS__
    idcorps = models.IntegerField(null=True, blank=True)
    libelle = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Corps_FIELDS__END

    class Meta:
        verbose_name        = _("Corps")
        verbose_name_plural = _("Corps")



#__MODELS__END
