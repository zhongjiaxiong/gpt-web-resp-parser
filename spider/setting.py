from environs import Env
from loguru import logger

env = Env()
env.read_env()

DEV_MODE, TEST_MODE, PROD_MODE = "dev", "test", "prod"
APP_ENV = env.str("APP_ENV", DEV_MODE).lower()
APP_DEBUG = env.bool("APP_DEBUG", True if APP_ENV == DEV_MODE else False)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_DEV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV = TEST_MODE

# logger
logger.add(env.str("LOG_RUNTIME_FILE", "runtime.log"), level="DEBUG", rotation="1 week", retention="20 days")
logger.add(env.str("LOG_ERROR_FILE", "error.log"), level="ERROR", rotation="1 week")

# test
API_DOMAIN = env.str("API_DOMAIN", None)
assert API_DOMAIN, "[!] API_DOMAIN is not set in .env file"
API_KEY = env.str("API_KEY", None)
assert API_KEY, "[!] API_KEY is not set in .env file"

# config.py
# PLATFORM OPENAI_MODEL OPENAI_API_KEY AIGC_MODEL AIGC_API_KEY TEMPERATURE TOP_P FREQUENCY_PENALTY PRESENCE_PENALTY
PLATFORM = env.str("PLATFORM", "openai")
OPENAI_MODEL = env.str("OPENAI_MODEL", "curie")
OPENAI_API_KEY = env.str("OPENAI_API_KEY", None)
assert OPENAI_API_KEY, "[!] OPENAI_API_KEY is not set in.env file"
AIGC_MODEL = env.str("AIGC_MODEL", "curie")
AIGC_API_KEY = env.str("AIGC_API_KEY", None)
assert AIGC_API_KEY, "[!] AIGC_API_KEY is not set in .env file"
TEMPERATURE = env.float("TEMPERATURE", 0.7)
TOP_P = env.float("TOP_P", 1.0)
FREQUENCY_PENALTY = env.float("FREQUENCY_PENALTY", 0.0)
PRESENCE_PENALTY = env.float("PRESENCE_PENALTY", 0.0)

