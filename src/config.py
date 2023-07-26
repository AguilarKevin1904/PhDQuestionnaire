class Config:
    SECRET_KEY = '7a7ac405cf314ca09914a78a2058111f'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask'

config={
    'development':DevelopmentConfig
}