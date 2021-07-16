from time import gmtime, strftime

from rest_framework import serializers

__all__ = [
    "serializers",
    "FormattedDurationField",
    "FormattedDatetimeField"
]


def check_spelling(duration):
    return '' if duration % 10 == 1 and duration % 100 != 11 else 's'


class FormattedDurationField(serializers.DurationField):
    def to_representation(self, value):
        if value.days and value.days >= 365:
            years = int(value.days // 365.25)
            return f"{years} year{check_spelling(years)}"
        if value.days and value.days < 365:
            return f"{value.days} day{check_spelling(value.days)}"
        if not value.days:
            return strftime("%H hours and %M minutes", gmtime(value.seconds))


class FormattedDatetimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%B %d, %Y")
