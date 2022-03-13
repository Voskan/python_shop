# Generated by Django 4.0.2 on 2022-02-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('code', models.CharField(max_length=12)),
                ('product_in', models.CharField(max_length=100)),
                ('in_stock', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='uploads/products/%Y/%m/%d')),
            ],
        ),
    ]