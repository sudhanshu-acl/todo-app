# Configuration settings

class Settings:
    def __init__(self):
        self.app_name = "Todo API"
        self.app_version = "1.0.0"
        self.debug = True
        self.database_url = "sqlite:///./test.db"
        self.secret_key = "YOUR_SUPER_SECRET_KEY_HERE"  # Change in production
        self.algorithm = "HS256"
        self.access_token_expire_minutes = 30

settings = Settings()
