# Generated by Django 3.0.6 on 2020-06-07 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_contactuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expiration_date',
        ),
    ]
