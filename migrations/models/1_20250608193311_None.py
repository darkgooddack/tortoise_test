from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "customer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "phone" VARCHAR(20)
);
COMMENT ON TABLE "customer" IS 'Модель Customer — клиент, покупающий соки.';
CREATE TABLE IF NOT EXISTS "order" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "customer_id" INT NOT NULL REFERENCES "customer" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "order" IS 'Модель Order представляет заказ клиента.';
CREATE TABLE IF NOT EXISTS "supplier" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "contact_info" TEXT NOT NULL
);
COMMENT ON TABLE "supplier" IS 'Модель Supplier — поставщик соков.';
CREATE TABLE IF NOT EXISTS "juice" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "price" DECIMAL(10,2) NOT NULL,
    "quantity" INT NOT NULL,
    "supplier_id" INT NOT NULL REFERENCES "supplier" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "juice" IS 'Модель Juice представляет сок в магазине.';
CREATE TABLE IF NOT EXISTS "orderitem" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quantity" INT NOT NULL,
    "juice_id" INT NOT NULL REFERENCES "juice" ("id") ON DELETE CASCADE,
    "order_id" INT NOT NULL REFERENCES "order" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "orderitem" IS 'Модель OrderItem представляет позицию в заказе — конкретный сок и его количество.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
