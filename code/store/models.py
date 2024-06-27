from django.db import models
from supplier.models import Supplier  # 从 supplier 应用导入 Supplier 模型

class Store(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Store ID')
    name = models.CharField(max_length=100, verbose_name='Store Name')
    location = models.CharField(max_length=200, verbose_name='Location')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    manager = models.CharField(max_length=100, verbose_name='Manager')
    suppliers = models.ManyToManyField(Supplier, related_name='stores', verbose_name='Suppliers')

    class Meta:
        verbose_name = '门店信息'
        verbose_name_plural = '门店信息'

    def __str__(self):
        return self.name
