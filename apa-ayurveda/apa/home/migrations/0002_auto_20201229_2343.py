# Generated by Django 3.1.4 on 2020-12-29 18:13

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(blank=True, default=None, upload_to=home.models.upload_location, verbose_name='Image_one'),
        ),
    ]