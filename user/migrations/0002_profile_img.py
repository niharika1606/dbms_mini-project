# Generated by Django 5.1.4 on 2025-03-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
