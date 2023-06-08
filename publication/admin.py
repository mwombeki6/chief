from django.contrib import admin
from .models import Publication, Category

admin.site.register(Category)

#class InnovationImageInline(admin.TabularInline):
#    model = Media

#@admin.register(Innovation)
#class InnovationAdmin(admin.ModelAdmin):
#    inlines = [
#        InnovationImageInline
#    ]    

admin.site.register(Publication)