# Generated by Django 4.0.2 on 2022-03-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ապրանքի բաժինը')),
            ],
            options={
                'verbose_name': 'Բաժին',
                'verbose_name_plural': 'Բաժիններ',
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Ապրանք', 'verbose_name_plural': 'Ապրանքներ'},
        ),
        migrations.AlterField(
            model_name='products',
            name='code',
            field=models.CharField(max_length=12, verbose_name='Ապրանքի կոդը'),
        ),
        migrations.AlterField(
            model_name='products',
            name='count',
            field=models.IntegerField(verbose_name='Քանակը'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, verbose_name='Նկարագրությունը'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='uploads/products/%Y/%m/%d', verbose_name='Նկարը'),
        ),
        migrations.AlterField(
            model_name='products',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='Առկա է, թե ոչ'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ապրանքի անունը'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Գինը ($)'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_in',
            field=models.CharField(max_length=100, verbose_name='Արտադրման երկիրը'),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Ապրանքի բաժինը'),
        ),
    ]
