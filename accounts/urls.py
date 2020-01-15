from django.urls import path
from . import views

urlpatterns = [
        path('send_login_email',views.send_login_email,name='send_login_email'),
        path('login',views.login,name='login'),
        #path('<int:list_id>/',views.view_list,name='view_list'),
]
