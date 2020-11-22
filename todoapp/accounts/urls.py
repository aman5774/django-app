from django.urls import path
from .views import login_view, logout_view

# app name to be used for url templating
app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
]
