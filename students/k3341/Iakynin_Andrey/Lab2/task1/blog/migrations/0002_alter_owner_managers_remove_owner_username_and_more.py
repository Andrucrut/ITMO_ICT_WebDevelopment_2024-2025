# Generated by Django 5.1.2 on 2024-10-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='owner',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='owner',
            name='username',
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
