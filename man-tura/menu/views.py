from django.views.generic import ListView
from for_user.models import RestaurantInfo
from django.http import HttpResponse

from .models import*
class ShowAllMenu(ListView):
    '''Для показа всех блюд'''
    model = Product
    template_name = 'menu/menu.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        context['category_selected'] = 0
        context['rest_info'] = RestaurantInfo.objects.all()[0]
        context['path_pref'] = '../'
        context['showing_all_menu'] = True

        session_key = self.request.session.session_key
        if not session_key:
            print(session_key)
            self.request.session.cycle_key()
        context['session_key'] = session_key
        # context['amount_product_in_cart'] = get_amount_product(self.request)
        

        context['categories'] = Category.objects.order_by('serial_number')
        return context


# class ShowCategory(ListView):
#     '''Для показа блюд конкретной категории'''
#     model = Product
#     template_name = 'menu/menu.html'
#     context_object_name = 'products'
    
#     def get_queryset(self):
#         return Product.objects.filter(cat__slug = self.kwargs['cat_slug'])
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c = Category.objects.get(slug = self.kwargs['cat_slug'])
#         context['title'] = c.name
#         context['category_selected'] = c.pk
#         context['categories']= Category.objects.order_by('serial_number')
#         context['rest_info'] = RestaurantInfo.objects.all()[0]
#         context['path_pref'] = '../../'


#         session_key = self.request.session.session_key
#         if not session_key:
#             self.request.session.cycle_key()
#         return context

#Функция для добавления блюда в корзину
def add_to_cart(request):

    session_key = request.session.session_key

    data = request.POST
    product_name = data.get('product_name')
    product_qty = data.get('product_qty')
    product_in_cart = ProductInCart.objects.filter(session_key=session_key, name=product_name)
    if not product_in_cart:
        ProductInCart.objects.create(session_key=session_key,name=product_name,quantity=product_qty)
    else:
        new_quantity = product_in_cart[0].quantity + int(product_qty)
        product_in_cart.update(quantity = new_quantity)
        
        
    return HttpResponse(None)