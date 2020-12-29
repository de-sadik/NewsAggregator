# Generated by Django 2.2.4 on 2020-11-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201118_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=400, unique=True)),
                ('image_url', models.URLField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
