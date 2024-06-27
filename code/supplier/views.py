from django.shortcuts import render, redirect
from login.models import User
from .models import Supplier
from django.db import transaction

def supplier_index(request):
    info = {"fields": Supplier._meta.fields, "suppliers": {}}
    if not User.objects.filter(ip=request.META['REMOTE_ADDR']):
        return redirect("../")
    
    filters = {
        'name__icontains': request.GET.get('name', ''),
        'phone_number__icontains': request.GET.get('phone', ''),
        'email__icontains': request.GET.get('email', ''),
        'contact_person__icontains': request.GET.get('contact_person', ''),
    }
    filters = {k: v for k, v in filters.items() if v}
    
    orderby = request.GET.get('orderby', '')  # Default to 'id' if not provided
    order = request.GET.get('order', '')  # Default to 'asc' if not provided
    
    delete_id = request.GET.get('delete')
    if delete_id:
        Supplier.objects.filter(id=delete_id).delete()
    
    suppliers = Supplier.objects.filter(**filters)
    if orderby:
        suppliers = suppliers.order_by(f"{'' if order == 'asc' else '-'}{orderby}")
    
    info.update({
        "suppliers": suppliers,
        "name_filter": request.GET.get('name', ''),
        "phone_filter": request.GET.get('phone', ''),
        "email_filter": request.GET.get('email', ''),
        "contact_person_filter": request.GET.get('contact_person', ''),
        "orderby": orderby,
        "order": order,
    })
    
    return render(request, 'supplier_index.html', info)

def supplier_create(request):
    if not(User.objects.filter(ip=request.META['REMOTE_ADDR'])):
        return redirect("../")
    if request.method == "POST":
        supplier_data = {
            'name': request.POST.get("name"),
            'phone_number': request.POST.get("phone_number"),
            'email': request.POST.get("email"),
            'contact_person': request.POST.get("contact_person"),
            'address': request.POST.get("address"),
        }
        if Supplier.objects.filter(name=supplier_data['name']):
            supplier_data['nameerr'] = "Name already exists"
            return render(request, 'edit_supplier.html', supplier_data)
        new_supplier = Supplier.objects.create(**supplier_data)
        return redirect(f'../?id={new_supplier.id}')
    return render(request, 'edit_supplier.html')

def supplier_edit(request, supplierid):
    if not User.objects.filter(ip=request.META['REMOTE_ADDR']).exists():
        return redirect("../")
    with transaction.atomic():
        supplier = Supplier.objects.select_for_update(skip_locked=True).get(id=supplierid)
        if request.method == "POST":
            supplier_data = {
                'name': request.POST.get("name"),
                'phone_number': request.POST.get("phone_number"),
                'email': request.POST.get("email"),
                'contact_person': request.POST.get("contact_person"),
                'address': request.POST.get("address"),
            }
            if Supplier.objects.filter(name=supplier_data['name']).exclude(id=supplierid).exists():
                supplier_data['nameerr'] = "Name already exists"
                supplier_data['supplier'] = supplier
                return render(request, 'edit_supplier.html', supplier_data)
            for attr, value in supplier_data.items():
                setattr(supplier, attr, value)
            supplier.save()
            return redirect('supplier_index')
        return render(request, 'edit_supplier.html', {'supplier': supplier})
