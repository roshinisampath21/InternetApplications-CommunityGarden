# Generated by Django 5.0.6 on 2024-06-19 18:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garden_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="upload",
            old_name="uploaded_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="upload",
            old_name="image",
            new_name="photo",
        ),
        migrations.RenameField(
            model_name="upload",
            old_name="description",
            new_name="tip",
        ),
    ]
