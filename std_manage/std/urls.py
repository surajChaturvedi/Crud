
from django.urls import path
from .import views

urlpatterns = [
    # path('',views.index, name=''),
    path("",views.home,name="home"),
    path("navbar/",views.navbar, name="navbar"),
    path("userreg/",views.userreg, name="userreg"),
    path("insertuser/",views.insertuser, name="insertuser"),
    path("updateuser/",views.updateuser, name="updateuser"),
    path("deleteuser/",views.deleteuser, name="deleteuser"), 
    path("numberOfUser/",views.numberOfUser, name="numberOfUser"),
]
