


from django.urls import path
# Импортируем созданные нами представления
from .views import (NewsList, NewDetail, NewsCreate, NewsUpdate, NewsDelete)
from .views import upgrade_me

urlpatterns = [

   path('', NewsList.as_view()),

   path('<int:pk>', NewDetail.as_view()),

   path('create/', NewsCreate.as_view(), name='news_create'),

   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),

   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

   path('upgrade/', upgrade_me, name = 'upgrade')

]