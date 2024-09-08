from habits.apps import HabitsConfig
from django.urls import path


app_name = HabitsConfig.name

urlpatterns = [
    path('list/'),
    path('public/'),
    path('create/'),
    path('update/<int:pk>/'),
    path('delete/<int:pk>/'),
]
