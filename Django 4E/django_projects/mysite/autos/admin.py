from django.contrib import admin

from .models import Auto, Make


class AutoAdmin(admin.ModelAdmin):
    list_display = ["nickname", "make", "mileage", "comments"]
    list_filter = ["make"]
    search_fields = ["nickname"]


class AutoInline(admin.TabularInline):
    model = Auto
    extra = 2


class MakeAdmin(admin.ModelAdmin):
    inlines = [AutoInline]
    search_fields = ["name"]


admin.site.register(Auto, AutoAdmin)
admin.site.register(Make, MakeAdmin)
