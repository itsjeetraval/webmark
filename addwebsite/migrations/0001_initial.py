# Generated by Django 4.2.7 on 2023-12-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addweb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=100)),
                ('web_description', models.TextField()),
                ('web_url', models.URLField()),
            ],
        ),
    ]
