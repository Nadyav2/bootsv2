from django.urls import path
from bootsv3 import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('blog/', views.blog, name='my_blog'),
    path('shop/', views.shop, name='my_shop'),
    path('about/', views.about, name='my_about')

]
