# Generated by Django 3.2.13 on 2022-05-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('tools', models.CharField(max_length=250)),
            ],
        ),
    ]
