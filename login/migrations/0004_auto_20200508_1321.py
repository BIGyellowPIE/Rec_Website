# Generated by Django 2.2.7 on 2020-05-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_usersim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='channel',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='prefer',
            field=models.CharField(default='', max_length=256),
        ),
    ]
