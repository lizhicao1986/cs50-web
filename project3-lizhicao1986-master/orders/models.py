from django.db import models

PIZZA_CATEGORIES = (
    ('Regular', 'Reular'),
    ('Sicilian', 'Sicilian'),
)
SUB_CATEGORIES = (
    ('Cheese', 'Cheese'),
    ('Italian', 'Italian'),
)
SIZE = (
    ('Small', 'Small'),
    ('Large', 'Large'),
)

class Pizza(models.Model):
    category = models.CharField(max_length=64, choices=PIZZA_CATEGORIES, default='Regular')
    size = models.CharField(max_length=64, choices=SIZE, default='Small')
    def __str__(self):
        return f"{self.size} {self.category} pizza."

class Sub(models.Model):
    category = models.CharField(max_length=64, choices=SUB_CATEGORIES, default='Cheese')
    size = models.CharField(max_length=64, choices=SIZE, default='Small')
    def __str__(self):
        return f"{self.size} {self.category} sub."
