# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('AirMail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CountDialog', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x83\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x85', db_column=b'CountDialog')),
            ],
            options={
                'db_table': 'Information',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='dialogue',
            name='Receiver_id',
            field=models.ForeignKey(related_name='Receiver', default=None, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='Text',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', db_column=b'Text'),
            preserve_default=True,
        ),
    ]
