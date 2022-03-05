# Generated by Django 4.0.3 on 2022-03-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=60)),
                ('Course_Number', models.DecimalField(decimal_places=2, default=0, max_digits=10000)),
                ('Instructor_Name', models.CharField(blank=True, default='', max_length=60)),
                ('Duration', models.FloatField(blank=True, default='', max_length=100)),
            ],
        ),
    ]