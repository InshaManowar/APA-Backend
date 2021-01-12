# Generated by Django 3.1.4 on 2021-01-10 04:32

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_account_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
    ]
