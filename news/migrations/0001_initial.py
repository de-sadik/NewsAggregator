# Generated by Django 2.2.4 on 2020-11-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('source_url', models.URLField()),
            ],
        ),
    ]
