from django.db import models

class menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50,blank=True, null=True,choices=[
        ('Beverages', 'Beverages'),
        ('Tandoor', 'Tandoor'),
        ('Chinese', 'Chinese'),
        ('Desserts', 'Desserts'),
        ('Snacks', 'Snacks'),
        ('Salads', 'Salads'),
        ('Soups', 'Soups'),
        ('Main Course', 'Main Course'),
        ('Sides', 'Sides'),
        ('Breakfast', 'Breakfast'),
        ('Specials', 'Specials'),
    ])  # e.g., 'Beverages', 'Tandoor', etc.
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='staff_images/', blank=True, null=True)
    def __str__(self):
        return self.name
    
class customer(models.Model):
    name = models.CharField(max_length=100 ,null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class order(models.Model):
    customer = models.ForeignKey(customer,null=True,blank=True, on_delete=models.CASCADE, related_name='orders')
    items = models.TextField(null=True,blank=True)  # Store item names or IDs
    total = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.customers.name}"

