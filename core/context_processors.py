from .models import SiteSettings


def site_settings(request):
    """Робить налаштування сайту (у т.ч. фонове зображення) доступними у всіх шаблонах."""
    return {'site_settings': SiteSettings.load()}
