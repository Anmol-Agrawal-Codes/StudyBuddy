# Generated by Django 5.1.1 on 2024-10-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]
