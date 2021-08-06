from django.urls import path
from django.contrib import admin
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', account.views.home, name='home'),
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', account.views.logout, name='logout'),
]