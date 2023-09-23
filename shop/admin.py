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
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)