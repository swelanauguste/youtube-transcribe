# Generated by Django 4.2.1 on 2023-06-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audio", "0003_alter_audiotranscription_audio_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="audiotranscription",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
