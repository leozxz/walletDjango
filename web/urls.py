from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('register/', views.register, name='register' ),
    path('dashboard/', views.dashboard),
    path('dashboard/profile/', views.profile),
    path('dashboard/carteira/', views.carteira, name='carteira'),
    path('dashboard/comprar/', views.comprar),
    path('dashboard/vender/', views.vender),
]
