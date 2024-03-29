# Generated by Django 3.2.5 on 2021-07-30 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followingApp', '0002_alter_following_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL), related_name='usersFollowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
