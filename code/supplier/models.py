from django.db import models

class Supplier(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Supplier ID')
    name = models.CharField(max_length=100, verbose_name='Supplier Name')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email')
    contact_person = models.CharField(max_length=40, verbose_name='Contact Person')
    address = models.CharField(max_length=200, verbose_name='Address')

    class Meta:
        verbose_name = '供货商信息'
        verbose_name_plural = '供货商信息'

    def __str__(self):
        return self.name
