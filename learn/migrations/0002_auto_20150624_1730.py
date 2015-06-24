# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='username',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='uploadfile',
            field=models.FileField(upload_to=b'./learn/static/uploadfile'),
        ),
    ]
