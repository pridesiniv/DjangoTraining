# Generated by Django 4.1.5 on 2023-01-11 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MySuitCascade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtomeal',
            name='published',
            field=models.DateField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
