# Generated by Django 3.2 on 2021-04-17 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]