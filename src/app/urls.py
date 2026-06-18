from django.urls import path
from.views import home_page, name, year


urlpatterns = [
    path('', home_page, name='index'), # Пустые кавычки '' означают главную страницу
    # path('какой-адрес-будет-в-браузере/', имя_функции_представления, имя_ссылки)
    path('name/', name, name='name_page'), 
    path('year/', year, name='year_page'),
]

