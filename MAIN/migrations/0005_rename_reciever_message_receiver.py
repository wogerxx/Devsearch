# Generated by Django 5.1.3 on 2024-11-11 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MAIN", "0004_message_is_read_alter_message_sender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="reciever",
            new_name="receiver",
        ),
    ]
