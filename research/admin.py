from django.contrib import admin
from .models import Research, Media, Category

admin.site.register(Category)

#class InnovationImageInline(admin.TabularInline):
#    model = Media

#@admin.register(Innovation)
#class InnovationAdmin(admin.ModelAdmin):
#    inlines = [
#        InnovationImageInline
#    ]    

admin.site.register(Research)
admin.site.register(Media)