# Generated by Django 4.1.3 on 2022-11-11 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='location_id',
        ),
    ]