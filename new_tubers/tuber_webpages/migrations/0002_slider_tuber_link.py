# Generated by Django 3.1.6 on 2021-02-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuber_webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='tuber_link',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
