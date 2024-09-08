from celery import shared_task
from habits.models import Habit
from django.utils import timezone
from habits.services import tg_send


@shared_task
def go_habit():
    now = timezone.now()
    habits = Habit.objects.all()
    for habit in habits:
        if habit.user.tg_chat_id:
            if habit.time == now:
                tg_send(habit)
        else:
            print(f"Пользователь {habit.user.email} не указал свой тг.")
