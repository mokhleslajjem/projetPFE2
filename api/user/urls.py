from rest_framework.views import TokenRefreshView
from django.urls import path
from user import views




urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("dashboard/", views.dashboard),
]