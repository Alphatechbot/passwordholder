from django.urls import path
from .views import (indexview,
                    homepage,
                    addaccount,
                    view,
                    detailview,
                    deleteinfo,
                    updateinfo
                    )

app_name = 'base'

urlpatterns = [
    path('', indexview, name='index'),
    path('home/', homepage, name='home'),
    path('create/', addaccount, name='create'),
    path('view/', view, name='view'),
    path('detail/<int:id>/', detailview, name='detail'),
    path('delete/<int:id>/',deleteinfo, name='delete'),
    path('update/<int:id>/',updateinfo, name = 'update')


]
