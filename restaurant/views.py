from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order, Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login')
def home(request):
    return render(request, 'index.html', {})

@login_required(login_url='accounts/login')
def menu_item(request):
    menu = MenuItem.objects.all().order_by('-id')[:10]
    return render(request, 'menu.html', {'menu_item': menu})

@login_required(login_url='accounts/login')
def single_menu(request, pk):
    try:
        menu = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist as error:
        return error
    return render(request, 'single_menu.html', {'single_menu': menu})

@login_required(login_url='accounts/login')
def order(request, menu_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        menu_item = get_object_or_404(MenuItem, pk=menu_id)
        Order.objects.get_or_create(menu_item=menu_item, quantity=quantity, user=request.user)
        messages.success(request, f'You have successfully place an order for {quantity} {menu_item.name}')
        return redirect('restaurant:menu_item')
    if request.method == 'GET':
        try:
            menu = MenuItem.objects.get(pk=menu_id)
        except MenuItem.DoesNotExist as error:
            return error
        return render(request, 'single_menu.html', {'single_menu', menu})

@login_required(login_url='accounts/login')    
def order_view(request):
    order = Order.objects.select_related('menu_item').filter(user=request.user).all()
    return render(request, 'order.html', {'orders': order})
    
@login_required(login_url='accounts/login')    
def reservations(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        table_number = request.POST.get('table_number')
        time = request.POST.get('time')
        people = request.POST.get('people')
        Reservation.objects.get_or_create(customer_name=name, table_number=table_number, reservation_time=time, guest_count=people)
        messages.success(request, f'You have successfully make a reservation')
        return redirect('/')


    
