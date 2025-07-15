
import math
from .config import HEAT_OFFSET_PER_TREE_C, PLANT_CO2_ABSORPTION

def calculate_tree_need(current_temp, target_reduction=1.0):
    return math.ceil(target_reduction / HEAT_OFFSET_PER_TREE_C)

def suggest_plants(tree_count):
    each_type = math.ceil(tree_count / len(PLANT_CO2_ABSORPTION))
    result = {}
    for tree, rate in PLANT_CO2_ABSORPTION.items():
        result[tree] = {
            "count": each_type,
            "total_CO2_absorption_kg": round(each_type * rate, 2)
        }
    return result
