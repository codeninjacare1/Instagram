# Generated by Django 5.2 on 2025-06-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0006_profile_last_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='authy.profile'),
        ),
    ]
