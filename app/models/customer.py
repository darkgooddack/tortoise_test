from tortoise import fields, models

class Customer(models.Model):
    """
    Модель Customer — клиент, покупающий соки.

    Атрибуты:
        id (int): уникальный идентификатор клиента.
        name (str): имя клиента.
        email (str): email клиента (уникальный).
        phone (str | None): телефон клиента (необязательное поле).
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    phone = fields.CharField(max_length=20, null=True)