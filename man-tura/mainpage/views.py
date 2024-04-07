from django.shortcuts import render
from for_user.models import RestaurantInfo,SliderContent
# Показываем главную страницу
def show_mainpage(request):
    context = {
        'title':'Ресторан Мануфактура',
        'path_pref': '../../',
        'rest_info': RestaurantInfo.objects.all()[0],
        'slider_images':SliderContent.objects.all(),

    }
        

    return render(request,'mainpage/home.html',context=context)
