from freenit.base_config import Auth, Mail, BaseConfig as FreenitBaseConfig
from freenit.base_config import LDAP


class BaseConfig(FreenitBaseConfig):
    name = "NAME"
    version = "0.0.1"
    user = "freenit.models.ldap.user"
    role = "freenit.models.ldap.role"


class DevConfig(BaseConfig):
    debug = True
    auth = Auth(False)
    dburl = "sqlite:///db.sqlite"


class TestConfig(BaseConfig):
    debug = True
    auth = Auth(False)
    dburl = "sqlite:///test.sqlite"


class ProdConfig(BaseConfig):
    secret = "MORESECURESECRET" #nosec
    mail = Mail()
