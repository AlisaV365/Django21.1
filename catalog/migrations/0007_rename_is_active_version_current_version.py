# Generated by Django 4.2.3 on 2023-07-28 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_version_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='is_active',
            new_name='current_version',
        ),
    ]
