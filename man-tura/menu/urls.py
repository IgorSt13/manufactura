from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    # path('', cache_page(60*60*1.5)(ShowAllMenu.as_view()),name='all_menu'),
    # path('<slug:cat_slug>/', cache_page(60*60*1.5)(ShowCategory.as_view()),name='category'),
    path('add_to_cart',add_to_cart,name='add_to_cart'),
    path('', ShowAllMenu.as_view(),name='all_menu'),
    # path('<slug:cat_slug>/', ShowCategory.as_view(),name='category'),
]