# Generated by Django 4.2.3 on 2023-08-01 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_current_version_version_active_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт'),
        ),
    ]
