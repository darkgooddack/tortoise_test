from tortoise import fields, models

class Order(models.Model):
    """
    Модель Order представляет заказ клиента.

    Атрибуты:
        id (int): уникальный идентификатор заказа.
        created_at (datetime): дата и время создания заказа.
        customer (Customer): клиент, оформивший заказ (ForeignKey).
    """
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    customer = fields.ForeignKeyField("models.Customer", related_name="orders")


class OrderItem(models.Model):
    """
    Модель OrderItem представляет позицию в заказе — конкретный сок и его количество.

    Атрибуты:
        id (int): уникальный идентификатор позиции заказа.
        order (Order): заказ, к которому относится позиция (ForeignKey).
        juice (Juice): сок, заказанный в позиции (ForeignKey).
        quantity (int): количество заказанного сока.
    """
    id = fields.IntField(pk=True)
    order = fields.ForeignKeyField("models.Order", related_name="items")
    juice = fields.ForeignKeyField("models.Juice", related_name="order_items")
    quantity = fields.IntField()
