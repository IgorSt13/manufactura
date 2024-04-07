from django import template
from menu.models import ProductInCart
register = template.Library()
@register.simple_tag(takes_context=True)
def get_amount_prod_in_cart(context):
    try:
        products = ProductInCart.objects.filter(session_key=context['session_key'])
        if not products:
            return 0
        else:
            quantity_of_all_prod = 0
            for prod in products:
                quantity_of_all_prod += prod.quantity
            # print(context['session_key'])
            return quantity_of_all_prod
    except KeyError:
        None