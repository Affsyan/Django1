# Generated by Django 3.2.4 on 2021-07-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
