from django.contrib import admin
from django.urls import path,include
from products import views

app_name="products"
urlpatterns = [
    # path('', views.assortall, name='assort'),
    
    # path('<slug:category_slug>',views.assort, name='assort'),
    path('search/',views.assort, name='search'),
    path('<slug:category_slug>/<slug:subcategory_slug>/',views.assort, name='assort'),
    path('<slug:category_slug>/',views.assort, name='assort'),
    path('product/<slug:product_slug>',views.product,name="product"),
    
    

]