# Generated by Django 5.0.4 on 2024-06-27 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('user', '0002_remove_customuser_user_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='in_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.lobby'),
        ),
    ]
