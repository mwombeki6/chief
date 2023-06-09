# Generated by Django 4.2 on 2023-06-13 09:32

import autoslug.fields
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
                        to="publication.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ["topic_name"],
            },
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                ("publication_name", models.CharField(max_length=255)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from="publication_name",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("abstract", models.TextField()),
                ("published_file", models.FileField(upload_to="publication/files")),
                ("pages", models.IntegerField(blank=True, null=True)),
                ("publisher", models.CharField(max_length=255)),
                ("published_at", models.DateField(default=django.utils.timezone.now)),
                ("authors", models.CharField(max_length=255, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="publication.category",
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
                "verbose_name": "Publication",
                "verbose_name_plural": "Publications",
                "ordering": ("-published_at",),
            },
        ),
    ]
