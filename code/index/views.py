from django.shortcuts import render, redirect
from login.models import User
from users.models import User as Customer
from books.models import Books
from orders.models import Orders, Details
import random, time, datetime
from django.utils import timezone
from store.models import Store
from random import choice

def index(request):
    href = 'home/' if User.objects.filter(ip=request.META['REMOTE_ADDR']) else 'accounts/login'
    return render(request, 'index.html', {"href": href})

def home(request):
    info = {}
    if User.objects.filter(ip=request.META['REMOTE_ADDR']):
        if request.method == "GET":
            if request.GET.get("business") == "1":
                num = random.randint(5, 10)
                for i in range(num):
                    init_time = ''.join(str(time.time()).split('.'))
                    time.sleep(0.01)
                    user = random.choice(list(Customer.objects.all()))

                    # 获取 Store 模型中的所有记录
                    all_stores = Store.objects.all()

                    # 随机选择一个 Store 实例
                    store = choice(all_stores) 
                    
                     # 获取第一个店铺作为默认值，你可以根据实际情况修改这里
                    new, created = Orders.objects.get_or_create(id=init_time,
                                                                date=timezone.now(),
                                                                user=user,
                                                                store=store,
                                                                confirm='0',
                                                                )
                    for j in range(random.randint(1, 5)):
                        book = random.choice(list(Books.objects.all()))
                        if user.vip == 1:
                            bookprice = book.price_vip
                        else:
                            bookprice = book.price
                        Details.objects.create(book=book,
                                               order=new,
                                               price=bookprice,
                                               count=random.randint(1, 20))
                info.update({"message": "%d more new orders are coming!" % num})
        return render(request, 'home.html', info)
    else:
        return redirect("../")