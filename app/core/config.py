# Configuration settings

class Settings:
    def __init__(self):
        self.app_name = "Todo API"
        self.app_version = "1.0.0"
        self.debug = True
        self.database_url = "sqlite:///./test.db"

settings = Settings()
