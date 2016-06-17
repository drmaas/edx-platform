# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0007_coursemode_bulk_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModeConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=255)),
                ('certificate', models.BooleanField(default=False, verbose_name='Certificate')),
                ('id_verification', models.BooleanField(default=False, verbose_name='ID Verification')),
                ('credit_eligible', models.BooleanField(default=False, verbose_name='Credit Eligible')),
                ('cohort', models.BooleanField(default=False, verbose_name='Cohort')),
                ('upsell_course_mode', models.ForeignKey(default=None, blank=True, to='course_modes.CourseModeConfig', null=True, verbose_name='Upsell Course Mode Config')),
            ],
        ),
        migrations.AddField(
            model_name='coursemode',
            name='course_mode_config',
            field=models.ForeignKey(default=None, blank=True, to='course_modes.CourseModeConfig', null=True, verbose_name='Course Mode Config'),
        ),
    ]
