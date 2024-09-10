from django.db import models
from CeleryCW import settings

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        **NULLABLE
    )
    place = models.CharField(max_length=200, verbose_name="место")
    time = models.DateTimeField(verbose_name="время")
    action = models.CharField(max_length=400, verbose_name="действие")
    is_enjoyable = models.BooleanField(
        default=False,
        verbose_name="признак приятности"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        **NULLABLE
    )
    periodicity = models.IntegerField(default=1, verbose_name="периодичность")
    reward = models.CharField(
        max_length=400,
        verbose_name="вознаграждение",
        **NULLABLE
    )
    time_to_complete = models.DurationField(verbose_name="время на выполнение")
    is_public = models.BooleanField(
        verbose_name="признак публичности",
        default=False
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}."

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
