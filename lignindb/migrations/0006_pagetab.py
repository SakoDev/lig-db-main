# Generated by Django 4.0.5 on 2023-10-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lignindb', '0005_ncbidb_pathways'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagetab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=200)),
                ('pathways', models.CharField(max_length=200)),
                ('gene', models.CharField(max_length=200)),
            ],
        ),
    ]
