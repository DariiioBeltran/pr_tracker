# Generated by Django 3.2.13 on 2022-04-27 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0008_rename_owner_lift_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lift',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lifts', to=settings.AUTH_USER_MODEL),
        ),
    ]
