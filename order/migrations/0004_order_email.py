# Generated by Django 3.0.7 on 2021-01-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210113_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]