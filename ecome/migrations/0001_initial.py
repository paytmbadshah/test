# Generated by Django 3.2.4 on 2021-06-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='website_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=500)),
            ],
        ),
    ]
