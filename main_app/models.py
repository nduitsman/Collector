from django.db import models
from django.contrib.auth.models import User

class Tool(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.DecimalField(max_digits = 15, decimal_places=2)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['price']

class Review(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField(max_length = 1000)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name = 'reviews')
    
    def __str__(self):
        return self.title
    
class Wishlist(models.Model):
    name = models.CharField(max_length=150)
    tools = models.ManyToManyField(Tool)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'wishlist', to_field='username')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'wishlist')
    
    def __str__(self):
        return self.name
        