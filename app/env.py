from os import getenv

DB_HOST = getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(getenv("DB_PORT", "3306"))
DB_USERNAME = getenv("DB_USERNAME", "coupon")
DB_PASSWORD = getenv("DB_PASSWORD", "coupon")
DB_DATABASE = getenv("DB_DATABASE", "coupon")
DB_LOCATION = "mysql+pymysql://localhost:3306"
