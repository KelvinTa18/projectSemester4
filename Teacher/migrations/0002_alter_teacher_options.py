# Generated by Django 5.0.6 on 2024-05-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'default_permissions': ('add',), 'permissions': (('can_view', 'can publish artikel'), ('can_edit', 'can edit artikel'))},
        ),
    ]
