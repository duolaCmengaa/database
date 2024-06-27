from django.shortcuts import render, redirect
from login.models import User
from .models import Store, Supplier
from django.db import transaction

def store_index(request):
    info = {"fields": Store._meta.fields, "stores": {}}
    if not User.objects.filter(ip=request.META['REMOTE_ADDR']):
        return redirect("../")

    filters = {
        'name__icontains': request.GET.get('name', ''),
        'location__icontains': request.GET.get('location', ''),
        'phone_number__icontains': request.GET.get('phone', ''),
        'manager__icontains': request.GET.get('manager', ''),
    }
    filters = {k: v for k, v in filters.items() if v}

    orderby = request.GET.get('orderby', '')
    order = request.GET.get('order', '')

    delete_id = request.GET.get('delete')
    if delete_id:
        Store.objects.filter(id=delete_id).delete()
        return redirect('.')

    stores = Store.objects.filter(**filters)
    if orderby:
        if order == 'asc':
            stores = stores.order_by(orderby)
        elif order == 'desc':
            stores = stores.order_by(f"-{orderby}")
    else:
        stores = stores.order_by("id")  # 默认按 id 排序

    order_toggle = 'desc' if order == 'asc' else 'asc'

    info.update({
        "stores": stores,
        "name_filter": request.GET.get('name', ''),
        "location_filter": request.GET.get('location', ''),
        "phone_filter": request.GET.get('phone', ''),
        "manager_filter": request.GET.get('manager', ''),
        "orderby": orderby,
        "order": order,
        "order_toggle": order_toggle,
    })
    return render(request, 'store_index.html', info)


def store_create(request):
    all_suppliers = Supplier.objects.all()  # 获取所有供应商
    if not User.objects.filter(ip=request.META['REMOTE_ADDR']):
        return redirect("../")
    if request.method == "POST":
        store_data = {
            'name': request.POST.get("name"),
            'location': request.POST.get("location"),
            'phone_number': request.POST.get("phone_number"),
            'manager': request.POST.get("manager"),
        }
        selected_supplier_ids = request.POST.getlist('suppliers')  # 获取选中的供应商ID
        if Store.objects.filter(name=store_data['name']).exists():
            context = {
                'nameerr': "Name already exists",
                'all_suppliers': all_suppliers,
                **store_data,
            }
            return render(request, 'edit_store.html', context)
        new_store = Store.objects.create(**store_data)
        new_store.suppliers.set(selected_supplier_ids)  # 设置商店的供应商
        new_store.save()
        return redirect(f'../?id={new_store.id}')
    else:
        return render(request, 'edit_store.html', {'all_suppliers': all_suppliers})

def store_edit(request, storeid):
    store = Store.objects.get(id=storeid)
    all_suppliers = Supplier.objects.all()
    selected_supplier_ids = list(store.suppliers.values_list('id', flat=True))

    if request.method == "POST":
        store.name = request.POST.get("name")
        store.location = request.POST.get("location")
        store.phone_number = request.POST.get("phone_number")
        store.manager = request.POST.get("manager")
        
        selected_suppliers = request.POST.getlist("suppliers")
        store.suppliers.set(selected_suppliers)
        
        store.save()
        return redirect('store_index')

    return render(request, 'edit_store.html', {
        'store': store, 
        'all_suppliers': all_suppliers, 
        'selected_supplier_ids': selected_supplier_ids
    })