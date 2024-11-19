# Generated by Django 5.1.3 on 2024-11-12 22:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MAIN", "0005_rename_reciever_message_receiver"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="receiver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="receiverd_message",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
