# Generated by Django 5.0.4 on 2024-04-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="org_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]