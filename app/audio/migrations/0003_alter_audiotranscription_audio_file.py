# Generated by Django 4.2.1 on 2023-06-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audio", "0002_remove_audiotranscription_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiotranscription",
            name="audio_file",
            field=models.FileField(max_length=255, upload_to="audio-files"),
        ),
    ]