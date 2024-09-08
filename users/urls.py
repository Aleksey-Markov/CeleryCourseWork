from users.apps import UsersConfig
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import UserCreateView, UserListView, UserRetrieveView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('list/', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user_retrieve'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
]
