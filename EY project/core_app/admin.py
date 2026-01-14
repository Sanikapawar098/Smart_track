from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, CitizenProfile, Citizen, Complaint


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'email', 'is_society_manager', 'is_citizen', 'is_staff')
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {'fields': ('is_society_manager', 'is_citizen')}),
    )


@admin.register(CitizenProfile)
class CitizenProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'area_address')


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'area', 'lane_number')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'description', 'get_customer_area', 'status')
    list_filter = ('status',)

    def get_customer_name(self, obj):
        return obj.customer.get_full_name() or obj.customer.username

    get_customer_name.short_description = 'name'

    def get_customer_area(self, obj):
        profile = getattr(obj.customer, 'citizenprofile', None)
        return profile.area_address if profile else ''

    get_customer_area.short_description = 'area'
