# Generated by Django 4.0.2 on 2022-02-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produs', models.CharField(max_length=100)),
                ('tip_produs', models.CharField(max_length=100)),
            ],
        ),
    ]
