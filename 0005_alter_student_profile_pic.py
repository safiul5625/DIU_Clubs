# Generated by Django 5.0.4 on 2024-05-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_userregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/new_logo.png', upload_to='profile_pic'),
        ),
    ]
