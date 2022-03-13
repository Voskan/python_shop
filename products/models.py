from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ապրանքի անունը')
    description = models.TextField(blank=True, verbose_name='Նկարագրությունը')
    count = models.IntegerField(verbose_name='Քանակը')
    price = models.IntegerField(verbose_name='Գինը ($)')
    code = models.CharField(max_length=12, verbose_name='Ապրանքի կոդը')
    product_in = models.CharField(max_length=100, verbose_name='Արտադրման երկիրը')
    in_stock = models.BooleanField(default=True, verbose_name='Առկա է, թե ոչ')
    image = models.ImageField(upload_to='uploads/products/%Y/%m/%d', verbose_name='Նկարը')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Ապրանքի բաժինը')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ապրանք'
        verbose_name_plural = 'Ապրանքներ'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ապրանքի բաժինը')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Բաժին'
        verbose_name_plural = 'Բաժիններ'