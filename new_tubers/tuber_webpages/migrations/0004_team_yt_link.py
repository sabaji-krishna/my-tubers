# Generated by Django 3.1.6 on 2021-02-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuber_webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
