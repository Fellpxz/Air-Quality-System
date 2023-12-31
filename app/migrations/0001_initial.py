# Generated by Django 4.2.4 on 2023-08-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp10', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mp25', models.DecimalField(decimal_places=2, max_digits=10)),
                ('o3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('co', models.DecimalField(decimal_places=2, max_digits=10)),
                ('no2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('so2', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
