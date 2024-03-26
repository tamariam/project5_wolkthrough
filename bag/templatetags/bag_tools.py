# from django import template

# register = template.Library()

# @register.filter(name='calc_subtotal')
# def calc_subtotal(price, quantity):
#     # Check if either price or quantity is a dictionary
#     if isinstance(price, dict) or isinstance(quantity, dict):
#         return 0  # Or any default value you prefer if one of them is a dictionary
#     else:
#         try:
#             return price * quantity
#         except TypeError:
#             return 0

from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity