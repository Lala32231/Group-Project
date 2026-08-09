from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'background_image', 'overlay_opacity']

    def has_add_permission(self, request):
        # singleton — заборонити створення другого запису
        return not SiteSettings.objects.exists()
