from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    SECRET_KEY: str

    PAYME_ID: str
    PAYME_KEY: str
    PAYME_ACCOUNT_FIELD: str = "order_id"
    PAYME_AMOUNT_FIELD: str = "total_cost"
    PAYME_ACCOUNT_MODEL: str = "order.models.Order"
    PAYME_ONE_TIME_PAYMENT: bool = True
    PAYME_DISABLE_ADMIN: bool = True
    PAYME_TEST_MODE: bool = False

    CLICK_SERVICE_ID: str
    CLICK_MERCHANT_ID: str
    CLICK_SECRET_KEY: str
    CLICK_ACCOUNT_MODEL: str = "order.models.Order"
    CLICK_AMOUNT_FIELD: str = "total_cost"
    CLICK_DISABLE_ADMIN: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
