DEBUG = True or False

USERNAME = 'user'
PASSWORD = 'pass'
SERVER = 'host'
DB = 'database'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha-chave"
