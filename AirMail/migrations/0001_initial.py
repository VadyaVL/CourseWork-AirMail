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
                ('Receiver_id', models.ForeignKey(related_name='Receiver', default=None, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Dialogue',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CountDialog', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x83\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x85', db_column=b'CountDialog')),
                ('CountUser', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xba\xd0\xbe\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x87\xd1\x96\xd0\xb2', db_column=b'CountUser')),
            ],
            options={
                'db_table': 'Information',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Text', models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', db_column=b'Text')),
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
