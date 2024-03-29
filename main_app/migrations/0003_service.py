# Generated by Django 5.0 on 2024-01-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_car_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service', models.CharField(choices=[('O', 'Oil Change'), ('T', 'Rotate Tires'), ('F', 'Check Fluids & Filters')], default='O', max_length=1)),
            ],
        ),
    ]
