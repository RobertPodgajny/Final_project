# Generated by Django 2.0.3 on 2018-03-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cushion',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
