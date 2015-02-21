# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Dialogue(models.Model):
    Established = models.DateTimeField(db_column='Established', null=False)
    CountMess = models.IntegerField(db_column='CountMess', default=0, null=False)
    ForReceiver = models.BooleanField(db_column="ForReceiver", default=True, null=False)
    Creator_id = models.ForeignKey(User, default=None,
                                   related_name='Creator', null=False)
    Receiver_id = models.ForeignKey(User, default=None,
                                    related_name='Receiver', null=True)

    class Meta:
        db_table = 'Dialogue'

    def __str__(self):
        str = ''
        tmp = Message.objects.filter(Dialogue_id=self)
        lenght = len(tmp)
        if lenght>=2:
            str = tmp[lenght-2].__str__() + "\n" + tmp[lenght-1].__str__()
        else:
            str = tmp[lenght-1].__str__()

        return str

    def Mess2(self):
        tmp = Message.objects.filter(Dialogue_id=self)
        lenght = len(tmp)
        if lenght>=1:
            return tmp[lenght-1]
        else:
            return

    def Mess1(self):
        tmp = Message.objects.filter(Dialogue_id=self)
        lenght = len(tmp)
        if lenght>=2:
            return tmp[lenght-2]
        else:
            return

class Message(models.Model):

    Text = models.CharField(db_column='Text', max_length=200, null=False, verbose_name='Повідомлення')
    DateSent = models.DateTimeField(db_column='DateSent', null=False);
    Dialogue_id = models.ForeignKey(Dialogue, null=False)
    User_id = models.ForeignKey(User, default=None, null=False)

    class Meta:
        db_table = 'Message'

    def __str__(self):
        return self.Text

class Information(models.Model):

    CountDialog = models.IntegerField(db_column='CountDialog', null=False, default=0, verbose_name='Кількість запущених')

    class Meta:
        db_table = 'Information'