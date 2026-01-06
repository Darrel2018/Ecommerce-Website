from django.contrib import admin

from .models import Category, Product, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'rating', 'product', 'created_at']
    list_filter = ['created_at']

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)