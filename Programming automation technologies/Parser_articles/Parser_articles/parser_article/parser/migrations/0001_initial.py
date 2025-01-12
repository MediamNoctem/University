# Generated by Django 5.1.4 on 2024-12-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=500)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('text', models.TextField()),
                ('source_url', models.URLField()),
            ],
        ),
    ]
