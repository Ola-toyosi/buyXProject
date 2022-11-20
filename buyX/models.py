from django.db import models
from django.conf import settings


# Create your models here.

# item you can purchase
class Item(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# item you've added to your cart
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    # link order to a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    # date order was created
    start_date = models.DateTimeField(auto_now_add=True)
    # date the items were ordered
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
