from dataclasses import dataclass
from typing import Optional


@dataclass
class Pokemon:
    pokedex_number: int
    generation: int
    primary_type: str
    sub_type: Optional[str]
    pokemon_name_english: str
    pokemon_name_korean: Optional[str]
    attack: int
    defense: int
    stamina: int
    is_mega: int
    level_20_cp: int
    level_30_cp: int
    level_35_cp: int
    level_40_cp: int
    purification_candy: int
    purification_dust: int
    buddy_km: int
    candy_for_evolution: int
    catch_rate: Optional[float]
    fleet_rate: float
    primary_move: str
    secondary_move: str
    detail_link: str
