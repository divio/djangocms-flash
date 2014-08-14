# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flash',
            fields=[
                ('file', models.FileField(help_text='use swf file', upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='file')),
                ('width', models.CharField(max_length=6, verbose_name='width')),
                ('height', models.CharField(max_length=6, verbose_name='height')),
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
