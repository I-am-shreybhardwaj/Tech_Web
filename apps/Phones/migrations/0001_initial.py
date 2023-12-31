# Generated by Django 4.1.7 on 2023-07-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone Name')),
                ('brand', models.CharField(blank=True, choices=[('Samsung', 'Samsung'), ('Apple', 'Apple')], max_length=30, null=True, verbose_name='Phone Brand')),
            ],
        ),
    ]
