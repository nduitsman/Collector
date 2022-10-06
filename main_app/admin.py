from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tool, Review, Wishlist, User


admin.site.register(Tool)
admin.site.register(Review)
admin.site.register(Wishlist)


