# Generated by Django 4.2.3 on 2023-09-09 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_subscription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='Subscribe',
        ),
    ]