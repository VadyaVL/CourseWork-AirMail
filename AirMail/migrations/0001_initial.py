# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Established', models.DateTimeField(db_column=b'Established')),
                ('CountMess', models.IntegerField(default=0, db_column=b'CountMess')),
                ('ForReceiver', models.BooleanField(default=True, db_column=b'ForReceiver')),
                ('Creator_id', models.ForeignKey(related_name='Creator', default=None, to=settings.AUTH_USER_MODEL)),
                ('Receiver_id', models.ForeignKey(related_name='Receiver', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Dialogue',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Text', models.CharField(max_length=200, db_column=b'Text')),
                ('DateSent', models.DateTimeField(db_column=b'DateSent')),
                ('Dialogue_id', models.ForeignKey(to='AirMail.Dialogue')),
                ('User_id', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Message',
            },
            bases=(models.Model,),
        ),
    ]
