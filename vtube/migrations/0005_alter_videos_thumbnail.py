# Generated by Django 3.2.5 on 2022-02-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtube', '0004_videos_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='thumbnail',
            field=models.ImageField(default='', max_length=200, upload_to='public/videosThumbnail/'),
        ),
    ]