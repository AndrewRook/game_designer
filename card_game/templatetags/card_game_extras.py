from django import template
register = template.Library()

#Use in template as:
#{% if field.field.widget|fieldname == "ClearableFileInput" %}
@register.filter('fieldname')
def fieldname(ob):
    return ob.__class__.__name__
