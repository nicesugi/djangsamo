from django.contrib import admin
from product.models import Product as ProductModel
from product.models import Review as ReviewModel


admin.site.register(ProductModel)
admin.site.register(ReviewModel)