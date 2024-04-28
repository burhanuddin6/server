# Generated by Django 5.0.4 on 2024-04-28 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ats", "0007_candidate_first_name_candidate_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recruiter",
            name="org_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="ats.organization"
            ),
        ),
    ]