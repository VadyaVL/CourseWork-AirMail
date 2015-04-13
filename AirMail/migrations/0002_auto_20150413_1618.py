# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AirMail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='CountUser',
        ),
        migrations.AddField(
            model_name='information',
            name='CountU',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xba\xd0\xbe\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x87\xd1\x96\xd0\xb2', db_column=b'CountU'),
            preserve_default=True,
        ),
    ]
