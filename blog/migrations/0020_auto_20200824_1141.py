# Generated by Django 2.2.15 on 2020-08-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200824_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='images',
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='images/'),
        ),
    ]
