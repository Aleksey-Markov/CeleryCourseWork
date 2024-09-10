from rest_framework import serializers
from habits.models import Habit
from habits.validators import (
    RewardValidator,
    HabitRelatedValidator,
    EnjoyHabitValidator,
    PeriodicityValidator,
    DurationValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardValidator(val1="reward", val2="related_habit"),
            HabitRelatedValidator(val="related_habit"),
            DurationValidator(val="time_to_complete"),
            EnjoyHabitValidator(val="is_enjoyable"),
        ]
