# from django.shortcuts import render
# from .models import menu as MenuItem, staff, customer as customer1, order as order_view

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def menu(request):
#     categories = [
#         'Beverages', 'Tandoor', 'Chinese', 'Desserts', 'Snacks',
#         'Salads', 'Soups', 'MainCourse', 'Sides', 'Breakfast', 'Specials'
#     ]

#     context = { cat.lower().replace(" ", "_"): MenuItem.objects.filter(category__iexact=cat) for cat in categories }

#     return render(request, 'menu.html', context)

# def order(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         items = request.POST.get('items')
#         address = request.POST.get('address')

#         order_view.objects.create(name=name, phone=phone, items=items, address=address)

#         return render(request, 'order.html', {'success': True})

#     return render(request, 'order.html')
from django.shortcuts import render, redirect
from .models import menu as MenuItem, customer as cus, staff as Staff, order as OrderView

def home(request):
    return render(request, 'home.html')

def menu(request):
    categories = [
        'Beverages', 'Tandoor', 'Chinese', 'Desserts', 'Snacks',
        'Salads', 'Soups', 'MainCourse', 'Sides', 'Breakfast', 'Specials'
    ]
    context = { cat.lower().replace(" ", "_"): MenuItem.objects.filter(category__iexact=cat) for cat in categories }
    return render(request, 'menu.html', context)

def order(request):
    return render(request, 'order.html')


def staff(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff_members})

def customer(request):
    return render(request, 'customer.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
