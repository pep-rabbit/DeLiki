from pathlib import Path

import msgspec


class DataPathConfig(msgspec.Struct):
    path: str


class CORSConfig(msgspec.Struct):
    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]


class APIConfig(msgspec.Struct):
    cors: CORSConfig
    title: str = "DeLiki API"
    version: str = "0.1.0"


class Config(msgspec.Struct):
    api: APIConfig
    data: DataPathConfig


config = msgspec.yaml.decode(Path("./config.yaml").read_bytes(), type=Config)
