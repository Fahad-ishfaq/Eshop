# Generated by Django 3.0.6 on 2021-01-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210127_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
