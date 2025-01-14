
from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/1/
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    #add items
    path('add',views.Create_Item.as_view(),name='create_item'),
    
    path('update/<int:id>/',views.update_items,name='update_items'),
    path('delete/<int:id>/',views.delete_items,name='delete_items'),

]
