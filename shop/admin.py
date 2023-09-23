from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name','image','description')

# admin.site.register(Category,CategoryAdmin)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
admin.site.register(Product,ProductAdmin)

class CartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
admin.site.register(Cart,CartAdmin)

class FavouriteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
admin.site.register(Favourite,FavouriteAdmin)