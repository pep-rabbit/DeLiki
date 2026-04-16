from litestar import Litestar
from litestar.config.cors import CORSConfig
from src.core.config import config

from api.src.router.endpoint import router

app = Litestar(
    route_handlers=[router],
    cors_config=CORSConfig(
        config.cors.allow_origins,
        config.cors.allow_methods,
        config.cors.allow_headers,
    ),
)
