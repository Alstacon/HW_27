# Generated by Django 4.1.3 on 2022-11-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_location_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location_id',
            new_name='locations',
        ),
    ]