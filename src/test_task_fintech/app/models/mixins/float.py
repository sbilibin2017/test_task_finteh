from django.db.models import FloatField, Model  # type: ignore


class FloatMixin(Model):
    value: FloatField = FloatField(verbose_name="value")

    class Meta:
        abstract = True
