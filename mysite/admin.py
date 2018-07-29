from django.contrib import admin
from mysite import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','enable','pub_time')
    ordering = ('-pub_time',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel',"nickname","price","year")
    search_fields = ('nickname',)
    ordering = ('-price',)


admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)

admin.site.register(models.PModel)
admin.site.register(models.Product1, ProductAdmin)
admin.site.register(models.Maker)
admin.site.register(models.PPhoto)

admin.site.register(models.Product)
