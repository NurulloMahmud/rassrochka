# Generated by Django 4.2 on 2024-08-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
