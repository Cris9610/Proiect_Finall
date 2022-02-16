# Generated by Django 4.0.2 on 2022-02-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_pungi_cantitate_alter_pungi_tip_punga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pungi',
            name='cantitate',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Nr. Bucati (min. 10.000 buc)'),
        ),
        migrations.AlterField(
            model_name='pungi',
            name='eurohole',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pungi',
            name='zipper',
            field=models.BooleanField(default=0, null=True),
        ),
    ]