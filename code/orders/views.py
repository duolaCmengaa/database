

from django.shortcuts import render, redirect
from login.models import User
from users.models import User as us
from .models import *
from django.db import transaction
from orders.models import Details
from datetime import datetime
from django.db.models import Sum, F, Count
# Create your views here.


def index(request):
    info = {"fields": Orders._meta.fields}
    if not (User.objects.filter(ip=request.META["REMOTE_ADDR"])):
        return redirect("../")
    id_filter = ""
    date_filter = ""
    user_filter = ""
    store_filter = ""
    lastedit_filter = ""
    confirmed_filter = ""
    storename_filter = ""  # 添加 storename 变量
    orderby = ""
    orderby2 = ""
    order = ""
    order2 = ""
    confirm_id = None
    if request.method == "GET":
        user_filter = request.GET.get("user") if request.GET.get("user") else ""
        id_filter = request.GET.get("id") if request.GET.get("id") else ""
        date_filter = request.GET.get("date") if request.GET.get("date") else ""
        book_filter = request.GET.get("book") if request.GET.get("book") else ""
        lastedit_filter = (
            request.GET.get("lastedit") if request.GET.get("lastedit") else ""
        )
        confirmed_filter = (
            request.GET.get("confirmed") if request.GET.get("confirmed") else ""
        )
        storename_filter = request.GET.get("storename") if request.GET.get("storename") else ""  # 添加获取 storename 参数
        orderby = request.GET.get("orderby")
        order = request.GET.get("order")
        orderby2 = request.GET.get("orderby2")
        order2 = request.GET.get("order2")
        confirm_id = request.GET.get("confirm")
        info.update(
            {
                "user_filter": user_filter,
                "store_filter": store_filter,
                "orderby": orderby,
                "order": order,
                "lastedit_filter": lastedit_filter,
                "book_filter": book_filter,
                "confirm_filter": confirmed_filter,
                "orderby2": orderby2,
                "order2": order2,
                "id_filter": id_filter,
                "date_filter": date_filter,
                "storename_filter": storename_filter,  # 更新 info 字典
            }
        )

    if confirm_id:
        my_order = Orders.objects.get(id=confirm_id)
        if my_order.confirm == "0":
            enough = 1
            user_now = User.objects.filter(ip=request.META["REMOTE_ADDR"]).first()
            for book, detail in zip(my_order.book.all(), my_order.details_set.all()):
                count = detail.count
                if book.storage < count:
                    info.update({"message": "Not enough storage for %s" % book})
                    enough = 0
            if enough:
                for book, detail in zip(
                    my_order.book.all(), my_order.details_set.all()
                ):
                    count = detail.count
                    book.storage -= count
                    book.save()
                my_order.confirm = "1"
                my_order.lastedit = user_now
                my_order.save()

    orders = []
    if orderby:
        if order == "asc":
            orders.append(orderby)
        if order == "desc":
            orders.append("-" + orderby)
    if orderby2:
        if order2 == "asc":
            orders.append(orderby2)
        if order2 == "desc":
            orders.append("-" + orderby2)

    if not orders:
        orders.append("confirm")  # 默认按 confirm 升序排序
        orders.append("-date")
        
    filters = {}
    if id_filter:
        filters["id"] = int(id_filter)
    if date_filter:
        filters["date"] = date_filter
    if user_filter:
        filters["user__name__icontains"] = user_filter
    if lastedit_filter:
        filters["lastedit__email__icontains"] = lastedit_filter
    if confirmed_filter:
        filters["confirm__icontains"] = confirmed_filter
    if storename_filter:
        filters["store__name__icontains"] = storename_filter  # 添加 storename 筛选条件
    
    orders_queryset = Orders.objects.filter(**filters).order_by(*orders)
    
    info.update({"orders": orders_queryset})

    return render(request, "orders.html", info)




def summary(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    store_id = request.GET.get('store_id')  # 从表单中获取选定的门店ID

    orders = Orders.objects.all()

    # 根据日期范围过滤订单和订单详情
    if start_date and end_date:
        orders = orders.filter(date__range=[start_date, end_date])

    # 如果选定了特定门店，则进一步过滤
    if store_id:
        orders = orders.filter(store_id=store_id)

    # 获取总订单数
    total_orders = orders.count()

    # 获取所有订单中图书的总数和总金额
    total_books = orders.aggregate(Sum('details__count'))
    total_revenue = orders.aggregate(Sum('details__price'))

    # 按用户分组统计订单数，使用用户名称进行分组
    orders_by_user = orders.values('user__name').annotate(totalnum=Count('id'),total_money1=Sum(F('details__count') * F('details__price'))).order_by('-total_money1')

    sales_and_money_by_store = orders.values('store__name').annotate(
        total_counts=Sum('details__count'),
        total_money=Sum(F('details__count') * F('details__price'))
    ).order_by('-total_money')

    # 统计每本书的销售数量，基于过滤后的详情
    booksale = orders.values('book__title').annotate(
        total_sold=Sum('details__count')
    ).order_by('-total_sold')



    context = {
        'total_orders': total_orders,
        'total_books': total_books['details__count__sum'],
        'total_revenue': total_revenue['details__price__sum'],
        'orders_by_user': orders_by_user,
        'sales_by_store': sales_and_money_by_store,  # 添加门店销售量统计数据到上下文中
        'start_date': start_date,
        'end_date': end_date,
        'booksale':booksale
    }

    return render(request, 'summary.html', context)



def edit(request, orderid):
    order = Orders.objects.get(id=orderid)
    users = us.objects.all()
    books = Books.objects.all()
    stores = Store.objects.all()
    details = Details.objects.filter(order=order)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                order.date = request.POST.get('date')
                order.user_name = request.POST.get('user')
                order.store_id = request.POST.get('store')
                order.confirm = request.POST.get('confirm')
                order.lastedit = User.objects.filter(ip=request.META['REMOTE_ADDR']).first()
                order.save()

                details.delete()

                book_ids = request.POST.getlist('book')
                for book_id in book_ids:
                    count = request.POST.get('count_' + book_id)
                    price = request.POST.get('price_' + book_id)
                    Details.objects.create(order=order, book_id=book_id, count=count, price=price)

            return redirect('orders')

        except Exception as e:
            return render(request, 'editorders.html', {
                'order': order,
                'users': users,
                'books': books,
                'stores': stores,
                'details': details,
                'error': str(e)
            })

    return render(request, 'editorders.html', {
        'order': order,
        'users': users,
        'books': books,
        'stores': stores,
        'details': details
    })
