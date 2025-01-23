# Generated by Django 5.1.5 on 2025-01-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD'), ('jeu_de_plateau', 'Jeu de Plateau')], max_length=20)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
