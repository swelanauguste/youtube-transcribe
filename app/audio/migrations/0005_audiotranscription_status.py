# Generated by Django 4.2.1 on 2023-06-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_audiotranscription_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiotranscription',
            name='status',
            field=models.CharField(default='processing', max_length=20),
        ),
    ]
