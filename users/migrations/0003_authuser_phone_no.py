# Generated by Django 4.0.2 on 2022-02-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='phone_no',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
