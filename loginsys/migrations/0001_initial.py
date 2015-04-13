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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karma', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd0\xbc\xd0\xb0', db_column=b'karma')),
                ('countDialog', models.IntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd1\x96\xd1\x81\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe \xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x96\xd0\xb2', db_column=b'countDialog')),
                ('countMess', models.IntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd1\x96\xd1\x81\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8c', db_column=b'countMess')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Profile',
            },
            bases=(models.Model,),
        ),
    ]
