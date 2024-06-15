# Generated by Django 5.0.6 on 2024-06-02 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField()),
            ],
            options={
                'verbose_name': 'Бонус',
                'verbose_name_plural': 'Бонусы',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование бренда')),
            ],
            options={
                'verbose_name': 'Наименование',
                'verbose_name_plural': 'Наименования',
            },
        ),
        migrations.CreateModel(
            name='LegalFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование Юр лица')),
            ],
            options={
                'verbose_name': 'Наименование',
                'verbose_name_plural': 'Наименования',
            },
        ),
        migrations.CreateModel(
            name='GeoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип "АЗС, гипермаркет"')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('nomenclature', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номенклатура')),
                ('discount', models.CharField(max_length=50, verbose_name='Скидка')),
                ('nds', models.BooleanField(default=True, verbose_name='НДС')),
                ('coordinates', models.CharField(max_length=200, verbose_name='Координаты')),
                ('logo_photo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
                ('logo_link', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ссылка на лого')),
                ('status', models.BooleanField(default=True, verbose_name='Статус работы')),
                ('bonuses', models.ManyToManyField(related_name='geo_data', to='partner_map.bonus', verbose_name='Бонусы')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner_map.brand', verbose_name='Бренд')),
                ('legal_face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner_map.legalface', verbose_name='Юридическое лицо')),
            ],
            options={
                'verbose_name': 'Гео объект',
                'verbose_name_plural': 'Гео объекты',
            },
        ),
    ]
