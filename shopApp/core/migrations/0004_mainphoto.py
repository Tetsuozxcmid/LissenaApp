# Generated by Django 5.2 on 2025-04-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_image2_product_image3_product_image4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Название')),
                ('image', models.ImageField(upload_to='pagephotos/', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Фотка сайта',
            },
        ),
    ]
