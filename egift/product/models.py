from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name 

class Brand(models.Model):
    brand_name = models.CharField(max_length = 25)

    class Meta:
        db_table = "brand"

    def __str__(self):
        return self.brand_name

class Gifts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    gift_name = models.CharField(max_length=25)
    gift_price = models.FloatField()
    gift_qty = models.IntegerField()
    gift_availability = models.BooleanField(null=True)

    class Meta:
        db_table = "gifts"

    def __str__(self):
        return self.gift_name