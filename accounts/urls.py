from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import register
app_name = 'accounts'

urlpatterns = [
    # 장고에서 기본적으로 가지고 있는 로그인 관련 url 불러오기
    #path('',include('django.contrib.auth.urls')),

    # 필요한 뷰만 불러다가 사용하기
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]