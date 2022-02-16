# Generated by Django 4.0.2 on 2022-02-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_alter_pungi_cantitate_alter_pungi_eurohole_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folie',
            name='cantitate',
            field=models.PositiveBigIntegerField(default=0, null=True, verbose_name='Nr. kilograme'),
        ),
        migrations.AlterField(
            model_name='pungi',
            name='cantitate',
            field=models.PositiveBigIntegerField(default=0, null=True, verbose_name='Nr. Bucati (min. 10.000 buc)'),
        ),
    ]