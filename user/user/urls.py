from django.contrib import admin
from django.urls import path
from user_model import views as user_model_view
from user_login import views as user_login_view
from user_info import views as user_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregistration', user_model_view.registration_req, name='registration_req'),
    path('userlogin', user_login_view.user_login, name='user_login'),
    path('userinfo', user_info_view.user_info, name='user_info')
]
