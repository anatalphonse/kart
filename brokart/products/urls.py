from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.index,name='home'),   
    path('product_list',views.list_products,name='list_products')
]