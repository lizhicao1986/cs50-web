from django.db import models



class order(models.Model):
	ORDER_CHOICES = (('Regular', 'Regular'), ('Sicilian', 'Sicilian'), ('Sub', 'Sub'),\
	('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Platter', 'Platter'),)
	orderType = models.CharField(max_length=64, choices=ORDER_CHOICES, default='Regular')
	SIZE_CHOICES = (('Small', 'Small'), ('Large', 'Large'),)
	size = models.CharField(max_length=64, choices=SIZE_CHOICES, blank=True)
	TOPPINGS_CHOICES = (('Pepperoni', 'Pepperoni'), ('Sausage', 'Sausage'),)
	toppings = models.CharField(max_length=64, choices=TOPPINGS_CHOICES, blank=True)

	def __str__(self):
		return f"This order is a {self.size} {self.orderType}"

# Create your models here.
class pizza(models.Model):
	REGULAR = "Regular"
	SICILIAN = "Scilian"
	TYPE_CHOICES = ( (REGULAR, 'Regular'), (SICILIAN, 'Sicilian'),)
	SMALL = "Small"
	LARGE = "Large"
	SIZE = ( (SMALL, 'Small'), (LARGE, 'Large'),)
	pizzaType = models.CharField(max_length=64, choices=TYPE_CHOICES, default=REGULAR)
	size = models.CharField(max_length=64, choices=SIZE, default=SMALL)


	def __str__(self):
		#return f"{self.size}"
		return f"{self.size} {self.pizzaType} pizza."

class toppings(models.Model):
	toppings = models.CharField(max_length=64,  choices=(('Pepperoni', 'Pepperoni'),\
	('Sausage', 'Sausage'), ('Mushrooms','Mushrooms'),))
	pizzas = models.ManyToManyField(pizza, blank=True, related_name="toppings")
	def __str__(self):
		return f"{self.toppings}"

class subs(models.Model):
	CHEESE = "Cheese"
	ITALIAN = "Italian"
	TYPE_CHOICES = ( (CHEESE, 'Cheese'), (ITALIAN, 'Italian'),)
	SMALL = "Small"
	LARGE = "Large"
	SIZE = ( (SMALL, 'Small'), (LARGE, 'Large'),)
	size = models.CharField(max_length = 2, choices = SIZE, default=SMALL)
	subType = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CHEESE)

	def __str__(self):
		#return f"{self.size}"
		return f"{self.size} {self.subType} sub."

# class order(models.Model):
# 	pizza_order = models.ForeignKey(pizza, on_delete=models.CASCADE, related_name="pizza_orders", blank=True)
# 	sub_order = models.ForeignKey(subs, on_delete=models.CASCADE, related_name="sub_orders", blank=True)
# 	def __str__(self):
# 		return f"This order contains {self.pizza_order}, {self.sub_order}"
