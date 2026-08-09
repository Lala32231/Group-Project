from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(field, css_class):
    """Додає CSS-клас (наприклад, Bootstrap form-control) до поля форми."""
    try:
        return field.as_widget(attrs={'class': css_class})
    except AttributeError:
        return field
