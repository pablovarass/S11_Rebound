from django.contrib import admin
from .models import Book

# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'autor', 'valoracion','rating')
    list_filter = ('autor', 'valoracion', 'fecha_modificacion')

    def rating(self, obj):
        if obj.valoracion < 1000:
            return 'Baja'
        elif 1000 <= obj.valoracion <= 2500:
            return 'Media'
        else:
            return 'Alta'   

    
        
admin.site.register(Book, BookAdmin) # registro de los model separados por coma