# Generated by Django 3.1.7 on 2021-03-22 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210322_0500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_orrdered',
            new_name='date_ordered',
        ),
    ]