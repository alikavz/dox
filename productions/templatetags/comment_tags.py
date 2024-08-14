from django import template

register = template.Library()


@register.filter
def only_active_comments(cms):
    return cms.filter(active=True)
