# Generated by Django 3.2.9 on 2021-11-10 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shareApp', '0007_alter_filemodel_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='uploaded_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
