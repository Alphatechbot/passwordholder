from django.urls import path
from .views import registerform, loginuser, logoutuser

app_name = 'login'

urlpatterns = [
    path('register/', registerform, name='register'),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout')
]
