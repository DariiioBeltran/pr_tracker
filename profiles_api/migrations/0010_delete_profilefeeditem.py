# Generated by Django 3.2.13 on 2022-04-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0009_alter_lift_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileFeedItem',
        ),
    ]
