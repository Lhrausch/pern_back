# Generated by Django 4.0.3 on 2022-03-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('name1', models.CharField(max_length=32)),
                ('name2', models.CharField(max_length=32)),
                ('name3', models.CharField(max_length=32)),
                ('name4', models.CharField(max_length=255)),
            ],
        ),
    ]