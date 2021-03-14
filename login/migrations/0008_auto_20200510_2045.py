# Generated by Django 2.2.7 on 2020-05-10 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200509_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='word_cloud',
            name='change_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='修改时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_info',
            name='cloud_dict',
            field=models.CharField(blank=True, default=' ', max_length=256, verbose_name='词云字典'),
        ),
        migrations.AlterField(
            model_name='word_cloud',
            name='cloud_time',
            field=models.DateField(verbose_name='词云记录时间'),
        ),
    ]