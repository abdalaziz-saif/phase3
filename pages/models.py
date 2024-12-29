from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.PositiveIntegerField(default=0)
    details= models.CharField(max_length=255)
    comment = models.TextField(),
    category = models.CharField(max_length=100, null=True, blank=True)

    def _str_(self):
        return str (self.name)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total=models.PositiveIntegerField(default=0)
    def get_total_price(self):
        return self.quantity * self.product.price
