import msgspec
from litestar import Router, get
from src.core.logic import get_pharmacies
from src.router.response import PharmacyInfo


@get("/top-pharmacies")
async def top_pharmacies(
    city: str,
    medical_program: str,
) -> list[PharmacyInfo]:
    pharmacies = await get_pharmacies(city, medical_program)
    return msgspec.json.decode(
        pharmacies.write_json(), type=list[PharmacyInfo]
    )


router = Router(path="/api", route_handlers=[top_pharmacies])
