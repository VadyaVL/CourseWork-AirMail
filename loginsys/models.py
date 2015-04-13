# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    karma = models.IntegerField(db_column='karma', default=0, verbose_name='Карма')
    countDialog = models.IntegerField(db_column='countDialog', default=0, verbose_name='Надіслано листів')
    countMess = models.IntegerField(db_column='countMess', default=0, verbose_name='Надіслано повідомлень')

    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return "/profile/%i/" % self.pk

    class Meta:
        db_table = 'Profile'