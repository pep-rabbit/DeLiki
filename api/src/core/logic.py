import polars as pl
from src.core.config import config


async def get_pharmacies(
    city: str,
    medical_program: str,
) -> pl.DataFrame:
    return await (
        pl.scan_parquet(config.data.path)
        .filter(
            pl.col("division_settlement").str.to_lowercase() == city.lower()
        )
        .filter(
            pl.col("medical_programs_in_divisions")
            .list.eval(
                pl.element().str.contains(medical_program, literal=True),
                parallel=True,
            )
            .list.any()
        )
        .sort("activity_score")
        .head(5)
    ).collect_async()
