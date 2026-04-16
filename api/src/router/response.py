import msgspec


class PharmacyInfo(msgspec.Struct):
    legal_entity_name: str
    division_name: str
    division_addresses: str
    division_phone: str
    division_type: str
    division_settlement: str
    activity_score: float
