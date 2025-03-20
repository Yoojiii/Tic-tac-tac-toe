from authx import AuthX, AuthXConfig

conf = AuthXConfig()
conf.JWT_SECRET_KEY = "SECRET_KEY"
conf.JWT_ACCESS_COOKIE_NAME = "my_access_token"
conf.JWT_TOKEN_LOCATION = ["cookies"]
security = AuthX(config=conf)

