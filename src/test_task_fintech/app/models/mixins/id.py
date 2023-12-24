from uuid import uuid4  # type: ignore

from django.db.models import Model, UUIDField  # type: ignore


class IdMixin(Model):
    id: UUIDField = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        verbose_name="id",
    )

    class Meta:
        abstract = True
