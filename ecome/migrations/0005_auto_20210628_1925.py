# Generated by Django 3.2.4 on 2021-06-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecome', '0004_auto_20210628_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image1',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image2',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image3',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image4',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image5',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
        migrations.AlterField(
            model_name='website_content_image',
            name='ban_image6',
            field=models.ImageField(blank=True, default='banner/download.jpg', null=True, upload_to='content_image'),
        ),
    ]
