import requests
import re
from typing import Optional

from database.crud import CRUD
from dto.Pokemon import Pokemon


# 특이케이스, 세레비같이 이벤트성 포켓몬은 포획률이 비어있는거 같다...이친구는 그냥 0이라고 하자
def extract_number(value: str) -> Optional[int]:
    return None if value == "" else re.findall(r'\d+', value)[0]


def check_bool(value: str) -> bool:
    return False if value == "Off" else True


def check_contain_sub_type(value: str) -> bool:
    return True if "," in value else False


def check_rate_value_exist(value: str) -> bool:
    return True if value == "" else False


def extract_moves(value: str, index: int) -> str:
    moves = value.split(",")
    return moves[index].strip()


def calculate_shadow_attack(value: int) -> str:
    return str(int(value * 1.2))


def calculate_shadow_defense(value: int) -> str:
    return str(int(value * 0.8))


def extract_pokemon_data_full():
    db = CRUD()

    request = requests.get(
        url="https://gamepress.gg/sites/default/files/aggregatedjson/pokemon-data-full-en-PoGO.json?9180519481526947113"
    )
    results = request.json()
    pokemon_list = []
    for result in results:
        has_sub_type = check_contain_sub_type(result["field_pokemon_type"])
        result_tuple = (
            str(extract_number(result["number"])),
            str(extract_number(result["field_pokemon_generation"])),
            str(extract_moves(result["field_pokemon_type"], 0) if has_sub_type else result["field_pokemon_type"]),
            str(extract_moves(result["field_pokemon_type"], 1) if has_sub_type else None),
            str(result["title_1"]),
            str(result["atk"] if result["field_shadow_pokemon_"] == "Off" else calculate_shadow_attack(int(result["atk"]))),
            str(result["def"] if result["field_shadow_pokemon_"] == "Off" else calculate_shadow_defense(int(result["def"]))),
            str(result["sta"]),
            str(check_bool(result["is_mega"])),
            str(int(float(result["lvl20"]))),
            str(int(float(result["lvl30"]))),
            str(int(float(result["lvl35"]))),
            str(int(float(result["lvl40"]))),
            str(result["purification_candy"]),
            str(result["purification_dust"]),
            str(result["buddy"]),
            str(extract_number(result["evo_requirements"])),
            str(extract_number(result["catch_rate"])),
            str(extract_number(result["field_flee_rate"])),
            str(result["field_primary_moves"]),
            str(result["field_secondary_moves"]),
            str(result["title"])
        )
        pokemon_list.append(result_tuple)

    db.insert_gamepress(pokemon_list)


if __name__ == "__main__":
    extract_pokemon_data_full()
