# Generated by Django 3.1 on 2020-10-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlhandler', '0005_shorturl_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='session_key',
        ),
    ]
