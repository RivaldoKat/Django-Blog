# Generated by Django 2.1.5 on 2021-05-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0004_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
    ]
