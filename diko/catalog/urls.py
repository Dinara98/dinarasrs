from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^menus/$', views.MenuListView.as_view(), name='menus'),
    path(r'^menu/(?P<pk>\d+)$', views.MenuDetailView.as_view(), name='menu-detail'),
]