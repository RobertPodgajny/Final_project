# Generated by Django 2.0.3 on 2018-03-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_auto_20180322_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='glass',
            field=models.SmallIntegerField(choices=[(-1, 'brak szkła'), (0, 'zwykłe'), (1, 'antyrefleksyjne')]),
        ),
    ]