# Generated by Django 3.1.2 on 2020-10-29 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('editorjs', '0003_auto_20201027_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editornote',
            name='note_id',
            field=models.UUIDField(default=uuid.UUID('4ddeb345-e059-4b85-af4e-7142021669c3')),
        ),
    ]
