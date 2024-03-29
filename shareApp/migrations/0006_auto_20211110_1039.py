# Generated by Django 3.2.9 on 2021-11-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareApp', '0005_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='file_type',
            field=models.CharField(choices=[('assignment', 'ASSIGNMENT'), ('syllabus', 'SYLLABUS'), ('report', 'REPORT'), ('notice', 'NOTICE'), ('result', 'RESULT'), ('other', 'OTHER')], default='notice', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='github_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
