def roll_call_dwarves(names):
    for n in names:
        print(f"{names.index(n) + 1}. {n}")

def summon_captain_planet(planeteer_calls):
    list = [n.capitalize() + "!" for n in planeteer_calls]
    return list

def long_planeteer_calls(calls):
    for n in calls:
        if len(n) > 4:
            return True
    return False

def find_the_cheese(list):
    if "cheddar" in list:
        return "cheddar"
    elif "gouda" in list:
        return "gouda"
    elif "camembert" in list:
        return "camembert"
    else:
        return None
