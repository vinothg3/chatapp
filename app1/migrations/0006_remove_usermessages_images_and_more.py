# Generated by Django 4.1.7 on 2023-08-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_usermessages_files_usermessages_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessages',
            name='images',
        ),
        migrations.RemoveField(
            model_name='usermessages',
            name='video_file',
        ),
        migrations.AddField(
            model_name='usermessages',
            name='imagevideo',
            field=models.FileField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='usermessages',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
    ]
