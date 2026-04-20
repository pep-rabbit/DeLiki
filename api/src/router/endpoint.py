import logging

import msgspec
from litestar import Router, get
from src.core.logic import get_pharmacies
from src.router.schuma import PharmacyInfo

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


@get("/top-pharmacies")
async def top_pharmacies(
    city: str,
    medical_program: str,
) -> list[PharmacyInfo]:
    return msgspec.json.decode(
        (await get_pharmacies(city, medical_program)).write_json(),
        type=list[PharmacyInfo],
    )


router = Router(path="/api", route_handlers=[top_pharmacies])
