# Generated by Django 3.0.6 on 2020-05-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0012_auto_20200513_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
