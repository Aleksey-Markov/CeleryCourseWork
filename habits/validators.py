from datetime import timedelta
from rest_framework.serializers import ValidationError


class RewardValidator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __call__(self, *args, **kwargs):
        tmp_val1 = dict(*args).get(self.val1)
        tmp_val2 = dict(*args).get(self.val2)
        if tmp_val1 and tmp_val2:
            raise ValidationError("Нужно выбрать ЛИБО вознаграждение ЛИБО полезную привычку.")


class HabitRelatedValidator:
    def __init__(self, val):
        self.val = val

    def __call__(self, *args, **kwargs):
        tmp_val = dict(*args).get(self.val)
        if tmp_val:
            if not tmp_val.is_enjoyable:
                raise ValidationError("Связанная привычка может быть только для приятной привычки.")


class DurationValidator:
    def __init__(self, val):
        self.val = val

    def __call__(self, *args, **kwargs):
        tmp_val = dict(*args).get(self.val)
        if tmp_val:
            if tmp_val > timedelta(seconds=120):
                raise ValidationError("Продолжительность не может быть больше 2-х минут.")


class EnjoyHabitValidator:
    def __init__(self, val):
        self.val = val

    def __call__(self, *args, **kwargs):
        tmp_val = dict(*args).get(self.val)
        if tmp_val:
           our_value = dict(*args)
           if (
               our_value.get("reward") is not None or
               our_value.get("related_habit") is not None
           ):
               raise ValidationError("У приятной привычки не может быть связанной привычки или вознаграждения.")


class PeriodicityValidator:
    def __init__(self, val1, val2):
        self.val = val1
        self.val2 = val2

    def __call__(self, *args, **kwargs):
        frequency_in_days = 0
        num = dict(*args).get(self.val1)
        unit = dict(*args).get(self.val2)

        if num:
            if unit == "minutes":
                frequency_in_days = num / (60 * 24)
            elif unit == "hours":
                frequency_in_days = num / 24
            elif unit == "days":
                frequency_in_days = num

        if frequency_in_days > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
