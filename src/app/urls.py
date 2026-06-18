from django.urls import path
from.views import home_page, name


urlpatterns = [
    path('', home_page, name='index'), # Пустые кавычки '' означают главную страницу
    # path('какой-адрес-будет-в-браузере/', имя_функции_представления, имя_ссылки)
    path('name/', name, name='name_page'), 
]

