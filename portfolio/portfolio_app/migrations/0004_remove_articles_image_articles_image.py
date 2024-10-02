# Generated by Django 5.1.1 on 2024-10-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0003_rename_article_articles"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="articles",
            name="image",
        ),
        migrations.AddField(
            model_name="articles",
            name="image",
            field=models.ManyToManyField(to="portfolio_app.picture"),
        ),
    ]
