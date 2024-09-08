from habits.apps import HabitsConfig
from django.urls import path
from habits.views import (HabitCreateView, HabitListView, HabitPublicListView, HabitRetrieveView, HabitUpdateView,
                          HabitDeleteView)


app_name = HabitsConfig.name

urlpatterns = [
    path('list/', HabitListView.as_view(), name='list'),
    path('public/', HabitPublicListView.as_view(), name='public'),
    path('<int:pk>/', HabitRetrieveView.as_view(), name='detail'),
    path('create/', HabitCreateView.as_view(), name='create'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='delete'),
]
