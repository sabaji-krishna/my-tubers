# Generated by Django 3.1.6 on 2021-02-06 12:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuber_webpages', '0005_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/service/%Y/')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
