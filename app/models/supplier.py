from tortoise import fields, models

class Supplier(models.Model):
    """
    Модель Supplier — поставщик соков.

    Атрибуты:
        id (int): уникальный идентификатор поставщика.
        name (str): название поставщика.
        contact_info (str): контактная информация поставщика.
        juices (list[Juice]): соки, которые поставщик поставляет (обратная связь).
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    contact_info = fields.TextField()
    juices: fields.ReverseRelation["Juice"]  # обратная связь на соки