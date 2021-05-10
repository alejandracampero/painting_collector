# Generated by Django 3.2.2 on 2021-05-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210509_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=700)),
                ('dims', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
    ]
