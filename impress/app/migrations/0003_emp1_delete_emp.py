# Generated by Django 4.2.4 on 2023-08-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='emp',
        ),
    ]
