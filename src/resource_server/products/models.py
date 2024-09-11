from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.price} on {self.date}"
