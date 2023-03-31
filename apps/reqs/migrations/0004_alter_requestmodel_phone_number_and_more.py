# Generated by Django 4.1.7 on 2023-03-30 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reqs", "0003_requestmodel_country_requestmodel_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requestmodel",
            name="phone_number",
            field=models.CharField(
                db_index=True,
                help_text="Enter phone number in international format",
                max_length=20,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
                        regex="^\\+(?:[0-9] ?){6,14}[0-9]$",
                    )
                ],
                verbose_name="номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="requestmodel",
            name="role",
            field=models.CharField(
                choices=[("Participant", "участник"), ("Viewer", "зритель")],
                max_length=12,
                verbose_name="Роль",
            ),
        ),
    ]