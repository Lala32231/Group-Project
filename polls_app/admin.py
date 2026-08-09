from django.contrib import admin
from .models import Poll, PollOption


class PollOptionInline(admin.TabularInline):
    model = PollOption


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInline]
    list_display = ['question', 'created_by', 'is_active', 'created_at']
