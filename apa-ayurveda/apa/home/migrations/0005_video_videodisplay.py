# Generated by Django 3.1.4 on 2021-01-11 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201230_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='VideoDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.TextField(blank=True, default=None)),
                ('videos', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.video')),
            ],
        ),
    ]
