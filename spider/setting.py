from environs import Env

env = Env()
env.read_env()

API_DOMAIN = env.str("API_DOMAIN", None)
assert API_DOMAIN, "[!] API_DOMAIN is not set in .env file"
API_KEY = env.str("API_KEY", None)
assert API_KEY, "[!] API_KEY is not set in .env file"
