# Generated by Django 3.2.7 on 2021-09-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0004_delete_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255)),
                ('allowed_users', models.CharField(max_length=255)),
                ('total_users', models.CharField(max_length=255)),
                ('no_of_users', models.CharField(max_length=255)),
            ],
        ),
    ]
