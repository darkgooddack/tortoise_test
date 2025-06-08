from tortoise import fields, models

class Juice(models.Model):
    """
    Модель Juice представляет сок в магазине.

    Атрибуты:
        id (int): уникальный идентификатор.
        name (str): название сока.
        price (Decimal): цена за единицу.
        quantity (int): количество на складе.
        supplier (Supplier): поставщик сока.
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = fields.IntField()
    supplier = fields.ForeignKeyField("models.Supplier", related_name="juices")
