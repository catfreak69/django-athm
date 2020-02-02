# Generated by Django 2.2.9 on 2020-01-26 19:26

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ATHM_Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("reference_number", models.CharField(max_length=64, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PROCESSING", "processing"),
                            ("COMPLETED", "completed"),
                            ("REFUNDED", "refunded"),
                        ],
                        default="PROCESSING",
                        max_length=16,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("total", models.FloatField()),
                ("tax", models.FloatField(null=True)),
                ("refunded_amount", models.FloatField(null=True)),
                ("subtotal", models.FloatField(null=True)),
                ("metadata_1", models.CharField(max_length=64, null=True)),
                ("metadata_2", models.CharField(max_length=64, null=True)),
            ],
            options={
                "verbose_name": "ATH transaction",
                "verbose_name_plural": "ATH transactions",
            },
        ),
        migrations.CreateModel(
            name="ATHM_Item",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("description", models.CharField(max_length=128)),
                ("quantity", models.PositiveSmallIntegerField(default=1)),
                ("price", models.FloatField()),
                ("tax", models.FloatField(null=True)),
                ("metadata", models.CharField(max_length=64, null=True)),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_athm.ATHM_Transaction",
                    ),
                ),
            ],
            options={"verbose_name": "ATH item", "verbose_name_plural": "ATH items",},
        ),
    ]
