# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170602_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='position',
            field=models.IntegerField(choices=[(0, b'Administrator'), (1, b'Lecturer'), (2, b'Physician'), (3, b'Professor-Adjunct'), (4, b'Professor-Assistant'), (5, b'Professor-Associate'), (6, b'Professor-Full'), (7, b'Professor-Emeritus'), (8, b'Postdoc'), (9, b'Research Associate'), (10, b'Research Scientist'), (11, b'Student-Doctoral'), (12, b"Student-Master's"), (13, b'Student-Medical Doctor'), (14, b'Technician'), (15, b'Other')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.IntegerField(choices=[(0, b'Administrator'), (1, b'Lecturer'), (2, b'Physician'), (3, b'Professor-Adjunct'), (4, b'Professor-Assistant'), (5, b'Professor-Associate'), (6, b'Professor-Full'), (7, b'Professor-Emeritus'), (8, b'Postdoc'), (9, b'Research Associate'), (10, b'Research Scientist'), (11, b'Student-Doctoral'), (12, b"Student-Master's"), (13, b'Student-Medical Doctor'), (14, b'Technician'), (15, b'Other')]),
        ),
    ]