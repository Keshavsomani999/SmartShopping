# Generated by Django 4.0.4 on 2023-01-05 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_contact_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='Subject',
            new_name='subject',
        ),
    ]