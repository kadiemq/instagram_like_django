# Generated by Django 3.2.5 on 2021-07-30 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followingApp', '0003_alter_following_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(related_name='usersFollowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
