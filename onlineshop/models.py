from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampedModel):
    category_name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.category_name
    

class Product(TimeStampedModel):
    product_name = models.CharField(max_length=50)
    description = models.TextField(max_length=180)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name



class Order(TimeStampedModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField(max_length=180)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.id}"
    