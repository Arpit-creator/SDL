from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('create/', views.CREATE, name='create'),
    path('view/<str:pk>', views.VIEW, name='view'),
    path('delete/<str:pk>', views.DELETE, name='delete'),
    path('item/add/<str:pk>', views.ADD, name='add_itm'),
    path('item/remove/<str:pk>', views.REMOVE, name='remove_itm'),
    path('item/done/<str:pk>', views.DONE, name='done_itm'),
]
