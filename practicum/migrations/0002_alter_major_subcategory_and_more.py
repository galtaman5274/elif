# Generated by Django 5.0.6 on 2024-06-23 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='practicum.subcategory'),
        ),
        migrations.AlterField(
            model_name='majorcontent',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_contents', to='practicum.contenttype'),
        ),
    ]
