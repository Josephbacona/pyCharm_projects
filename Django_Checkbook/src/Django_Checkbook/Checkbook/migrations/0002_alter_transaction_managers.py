# Generated by Django 4.0.3 on 2022-03-10 21:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]