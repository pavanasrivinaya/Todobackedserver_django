# Generated by Django 3.1.4 on 2020-12-06 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20201206_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='user_id',
        ),
    ]