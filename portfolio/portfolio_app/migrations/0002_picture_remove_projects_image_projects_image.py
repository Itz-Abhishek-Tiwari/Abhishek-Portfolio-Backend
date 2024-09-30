# Generated by Django 5.1.1 on 2024-09-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Picture",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="uploads/")),
            ],
        ),
        migrations.RemoveField(
            model_name="projects",
            name="image",
        ),
        migrations.AddField(
            model_name="projects",
            name="image",
            field=models.ManyToManyField(to="portfolio_app.picture"),
        ),
    ]
