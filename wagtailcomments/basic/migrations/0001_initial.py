# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 06:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumchoicefield.fields
import wagtailcomments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField()),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.GenericIPAddressField()),
                ('status', enumchoicefield.fields.EnumChoiceField(enum_class=wagtailcomments.models.CommentStatus, max_length=10)),
                ('body', models.TextField()),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'swappable': 'WAGTAILCOMMENTS_MODEL',
            },
        ),
    ]