# Generated by Django 5.0.4 on 2024-04-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ats", "0003_user_is_setup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="org_name",
            field=models.CharField(max_length=64),
        ),
    ]
