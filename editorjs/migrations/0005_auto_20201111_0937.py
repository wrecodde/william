# Generated by Django 3.1 on 2020-11-11 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('editorjs', '0004_auto_20201029_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editornote',
            name='note_id',
            field=models.UUIDField(default=uuid.UUID('8588b514-1cfa-40d1-885f-d78048eb03d0')),
        ),
    ]
