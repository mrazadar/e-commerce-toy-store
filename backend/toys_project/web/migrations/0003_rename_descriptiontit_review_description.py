# Generated by Django 4.1.1 on 2022-09-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='descriptiontit',
            new_name='description',
        ),
    ]
