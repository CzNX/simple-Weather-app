
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name="index"),
    path('addname/',views.add,name="add"),
    path('<city_name>/delete/',views.delete,name="delete"),

]
