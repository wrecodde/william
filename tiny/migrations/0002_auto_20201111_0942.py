# Generated by Django 3.1.2 on 2020-11-11 09:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tiny', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinynote',
            name='public_id',
            field=models.UUIDField(default=uuid.UUID('7fc1b86b-51ca-4b05-a002-9188d6619131')),
        ),
    ]
