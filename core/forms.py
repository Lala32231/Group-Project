from django import forms
from .models import SiteSettings


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['site_title', 'background_image', 'overlay_opacity']
        labels = {
            'site_title': 'Назва порталу',
            'background_image': 'Фонове зображення (буде розтягнуте на весь екран)',
            'overlay_opacity': 'Затемнення фону (%), для читабельності тексту',
        }
