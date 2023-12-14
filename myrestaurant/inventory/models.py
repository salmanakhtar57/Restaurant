from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity_available = models.PositiveIntegerField()
    price = models.IntegerField(max_length=5)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=5)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeRequirement')

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.IntegerField()

    def __str__(self):
        return f"{self.menu_item.name} - {self.ingredient.name}"
    
class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    item_purchased = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.item_purchased.name} ({self.quantity_purchased})"