# Generated by Django 5.0.6 on 2024-07-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
