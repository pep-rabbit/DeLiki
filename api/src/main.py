from litestar import Litestar
from litestar.config.cors import CORSConfig
from src.core.config import config
from src.router.endpoint import router

app = Litestar(
    route_handlers=[router],
    cors_config=CORSConfig(
        config.api.cors.allow_origins,
        config.api.cors.allow_methods,
        config.api.cors.allow_headers,
    ),
)
