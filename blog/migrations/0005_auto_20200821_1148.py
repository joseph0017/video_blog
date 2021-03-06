# Generated by Django 2.2.15 on 2020-08-21 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200821_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='document',
            name='images',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='document',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
