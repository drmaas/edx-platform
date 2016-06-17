# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0008_auto_20160616_2109'),
        ('student', '0006_logoutviewconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseenrollment',
            name='course_mode',
            field=models.ForeignKey(verbose_name='Course Mode', blank=True, to='course_modes.CourseMode', null=True),
        ),
        migrations.AddField(
            model_name='historicalcourseenrollment',
            name='course_mode',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='course_modes.CourseMode', null=True),
        ),
    ]
