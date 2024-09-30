# Generated by Django 5.1.1 on 2024-09-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("institution", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("degree", models.CharField(max_length=100, null=True)),
                ("cgpa", models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("feedback", models.TextField()),
                ("professor", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("technologies", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="WorkExperience",
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
                ("company", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("project_title", models.CharField(max_length=100)),
                ("project_description", models.TextField(null=True)),
                ("image", models.ImageField(upload_to="uploads/")),
                ("skills", models.ManyToManyField(to="portfolio_app.skills")),
            ],
        ),
    ]
