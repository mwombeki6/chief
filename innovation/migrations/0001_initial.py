# Generated by Django 4.2 on 2023-06-07 11:08

import autoslug.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "topic_name",
                    models.CharField(
                        choices=[
                            ("computer-engineering", "computer-engineering"),
                            ("mining", "mining"),
                            ("mechanical-engineering", "mechanical-engineering"),
                            ("bioTechnology", "biotechnology"),
                        ],
                        max_length=250,
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from="topic_name",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="innovation.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ["topic_name"],
            },
        ),
        migrations.CreateModel(
            name="Innovation",
            fields=[
                ("innovation_name", models.CharField(max_length=255)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from="innovation_name",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("abstract", models.TextField()),
                ("innovation_file", models.FileField(upload_to="innovation/files")),
                (
                    "uploaded_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="innovation.category",
                    ),
                ),
                (
                    "uploaded_by",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Innovation",
                "verbose_name_plural": "Innovations",
                "ordering": ("-uploaded_at",),
            },
        ),
        migrations.CreateModel(
            name="Media",
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
                ("images", cloudinary.models.CloudinaryField(max_length=255)),
                ("alt_text", models.CharField(max_length=100)),
                (
                    "uploaded_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "innovation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="innovation.innovation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media",
                "verbose_name_plural": "Medias",
            },
        ),
    ]
