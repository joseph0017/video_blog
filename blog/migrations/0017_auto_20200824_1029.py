# Generated by Django 2.2.15 on 2020-08-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200824_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AddField(
            model_name='document',
            name='images',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]