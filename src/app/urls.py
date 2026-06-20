from django.urls import path
from.views import home_page, name, year, color_view, password_v


urlpatterns = [
    path('', home_page, name='index'), # Пустые кавычки '' означают главную страницу
    # path('какой-адрес-будет-в-браузере/', имя_функции_представления, имя_ссылки)
    path('name/', name, name='name_page'), 
    path('year/', year, name='year_page'),
    path('color/', color_view, name='color_page'),
    path('password', password_v, name='password_page'),
]

