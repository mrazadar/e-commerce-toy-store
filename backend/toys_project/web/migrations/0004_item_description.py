# Generated by Django 4.1.1 on 2022-09-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_descriptiontit_review_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
