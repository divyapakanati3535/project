# Generated by Django 3.1.2 on 2021-11-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaForm', '0002_auto_20211114_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='is_allowed_to_change_batch',
        ),
        migrations.AddField(
            model_name='yogaform',
            name='is_allowed_to_change_batch',
            field=models.BooleanField(default=False),
        ),
    ]