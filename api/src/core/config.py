from pathlib import Path

import msgspec


class DataPathConfig(msgspec.Struct):
    path: Path = Path("./data/data.parquet")


class CORSConfig(msgspec.Struct):
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class Config(msgspec.Struct):
    cors: CORSConfig
    data: DataPathConfig


config = msgspec.yaml.decode(Path("./config.yaml").read_bytes(), type=Config)
