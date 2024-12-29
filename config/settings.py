import json

# Загрузка конфигурации
with open("config/secrets.json") as f:
    SECRETS = json.load(f)

REDIS_HOST = "localhost"
REDIS_PORT = 6379
CACHE_TTL = 3600  # Время жизни кэша в секундах