from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    availability = models.BooleanField(default=1)
    
    def __str__(self):
        return self.name, self.description
    
    
class Order(models.Model):
    menu_item = models.ForeignKey(to=MenuItem, related_name='menu_item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=5, default=0, help_text=' 0 == Pending 1 == Confirmed 2 == Shipped 3 == Delivered')
    order_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.menu_item
    
class Reservation(models.Model):
    customer_name = models.CharField(max_length=50)
    table_number = models.IntegerField()
    reservation_time = models.DateTimeField()
    guest_count = models.IntegerField()
    
    def __str__(self):
        return self.customer_name
    
    
class Inventory(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    
    def __str__(self):
        return self.item_name
