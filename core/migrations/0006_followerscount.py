# Generated by Django 4.1.4 on 2023-01-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_profile_firstname_remove_profile_lastname"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]
