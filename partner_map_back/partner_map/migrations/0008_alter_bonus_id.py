# Generated by Django 5.0.6 on 2024-06-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_map', '0007_rename_legal_face_geodata_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
