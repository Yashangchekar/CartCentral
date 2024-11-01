from django.contrib import admin

from .models import Products,Order




# Register your models here.

admin.site.site_header="ecommerice site"
admin.site.site_title='ABC shopping'
admin.site.index_title='manage shopping'


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')
    list_display =('title','price','discount_price','category','description','image')
    search_fields=('title','price','discount_price','category','description','image')
    actions=('change_category_to_default',)
    list_editable=('price',)


admin.site.register(Products,ProductAdmin)
admin.site.register(Order)

