from django import template

register = template.library()


@register.filter
def trans_num(value):
    value = str(value)
    engtopersian = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(engtopersian)
