from .base_config import ProdConfig as ProdConfigBase


class ProdConfig(ProdConfigBase):
    user = "freenit.models.sql.user"
    role = "freenit.models.sql.role"
