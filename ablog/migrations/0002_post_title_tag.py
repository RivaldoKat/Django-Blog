# Generated by Django 2.1.5 on 2021-03-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="I'm the stone that builder refused!!!! ", max_length=255),
        ),
    ]
