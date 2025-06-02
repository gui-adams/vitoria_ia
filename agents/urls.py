from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # / exibe o dashboard
    path('<str:id>/', views.agent_page, name='agent_page'),
    path('<str:id>/query/', views.agent_proxy, name='agent_proxy'),
]
