from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModel inside CarMake admin page
class CarModelInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = CarModel
    extra = 1  # Shows one extra blank CarModel form

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Customize if you add more fields
    inlines = [CarModelInline]

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make')
    list_filter = ('type', 'year', 'car_make')  # Optional but useful
    search_fields = ('name',)

# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
