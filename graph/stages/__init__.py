from .biotech import BIOTECH_STAGES
from .mature_mbo import MATURE_MBO_STAGES
from .real_estate import REAL_ESTATE_STAGES

STAGE_REGISTRY: dict[str, list[dict]] = {
    "biotech": BIOTECH_STAGES,
    "mature_mbo": MATURE_MBO_STAGES,
    "real_estate": REAL_ESTATE_STAGES,
}

DEAL_TYPE_ALIASES: dict[str, str] = {
    "biotech": "biotech",
    "mature_mbo": "mature_mbo",
    "mbo": "mature_mbo",
    "real_estate": "real_estate",
    "re": "real_estate",
    "paris_office": "real_estate",
    "paris": "real_estate",
}


def get_stages(deal_type: str) -> list[dict]:
    key = deal_type.lower().replace(" ", "_").replace("-", "_")
    resolved = DEAL_TYPE_ALIASES.get(key, key)
    if resolved not in STAGE_REGISTRY:
        raise ValueError(
            f"Unknown deal type: '{deal_type}'. "
            f"Valid options: {list(STAGE_REGISTRY.keys())}"
        )
    return STAGE_REGISTRY[resolved]
