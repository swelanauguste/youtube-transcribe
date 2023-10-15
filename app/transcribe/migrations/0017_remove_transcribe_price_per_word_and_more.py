# Generated by Django 4.2.6 on 2023-10-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcribe', '0016_alter_transcribe_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcribe',
            name='price_per_word',
        ),
        migrations.AddField(
            model_name='transcribe',
            name='price_per_min',
            field=models.DecimalField(decimal_places=5, default=0.5, max_digits=9),
        ),
    ]