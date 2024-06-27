from django.db import models
from login.models import User
from users.models import User as CustomUser
from store.models import Store
from books.models import Books  # 假设这是你的 Books 模型



from django.db import models

# Create your models here.


class Orders(models.Model):
    CONFIRMATION = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    id = models.CharField(max_length=64, verbose_name='Order ID', primary_key=True)
    lastedit = models.ForeignKey(to="login.User", verbose_name='Last Edit', on_delete=models.CASCADE, null=True)
    date = models.DateField(verbose_name='Date')
    user = models.ForeignKey(to="users.User", verbose_name='User', on_delete=models.CASCADE)
    book = models.ManyToManyField(to="books.Books", through="Details", through_fields=('order', 'book'),
                                  verbose_name='Books')
    store = models.ForeignKey(Store, verbose_name='Store', on_delete=models.CASCADE)  # 添加外键字段指向 Store 模型
    confirm = models.CharField(max_length=1, choices=CONFIRMATION, verbose_name='Confirmation', default='N')

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'
        ordering = ['-confirm']  # 按 confirm 升序排序

class Details(models.Model):
    book = models.ForeignKey(to='books.Books', on_delete=models.CASCADE)
    order = models.ForeignKey(to='orders.Orders', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    count = models.PositiveIntegerField(verbose_name='Count', default=0)