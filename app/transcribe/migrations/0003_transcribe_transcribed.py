# Generated by Django 4.2.1 on 2023-05-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transcribe", "0002_transcribe_video_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="transcribe",
            name="transcribed",
            field=models.TextField(blank=True, null=True),
        ),
    ]
