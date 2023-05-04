# Generated by Django 4.2.1 on 2023-05-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transcribe", "0010_transcribe_price_per_word_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transcribe",
            name="price_per_word",
            field=models.DecimalField(decimal_places=5, default=0.04, max_digits=9),
        ),
    ]
