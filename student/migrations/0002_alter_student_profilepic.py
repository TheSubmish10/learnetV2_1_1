# Generated by Django 4.2.5 on 2023-09-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profilepic',
            field=models.ImageField(default='profilepic\\profile.jpg', upload_to='profilepic/'),
        ),
    ]
