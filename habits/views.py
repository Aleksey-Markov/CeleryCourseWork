from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner
from habits.paginators import MyPagination


class HabitCreateView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = MyPagination


class HabitRetrieveView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDeleteView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
