# Generated by Django 5.0.6 on 2024-06-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_map', '0008_alter_bonus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
