from math import inf
from random import randint

tables = {
    "sizes": {
        .5: "fine",
        1: "diminutive",
        2: "tiny",
        4: "small",
        8: "medium",
        16: "large",
        32: "huge",
        64: "gargantuan",
        inf: "colossal"
    },
    
    "shades": {
        1: "",
        2: "pale ",
        3: "bright ",
        4: "light ",
        5: "dark ",
        6: "glossy "
    },
    
    "colors": {
        1: "${shades}red",
        2: "${shades}yellow",
        3: "${shades}green", 
        4: "${shades}blue",
        5: "${shades}purple",
        6: "${shades}pink",
        7: "white",
        8: "black",
        9: "${shades}brown"
    },
    
    "seasons": {
        1: "early winter",
        2: "late winter",
        3: "early spring",
        4: "late spring",
        5: "early summer",
        6: "late summer",
        7: "early fall",
        8: "late fall"
    },
    
    "symptoms": {
        1: "shock",
        2: "fever",
        3: "pain",
        4: "nausea",
        5: "rash",
        6: "hallucinations",
        7: "nightmares",
        8: "drowsiness",
        9: "slow heart rate",
        10: "fast heart rate",
        11: "high blood pressure",
        12: "low blood pressure",
        13: "clotting",
        14: "headache",
        15: "vomiting"
    },
    
    "boons": {
        1: "invisibility",
        2: "resistance to ${damages}",
        3: "vulnerability to ${damages}",
        4: "regeneration"
    },
    
    "damages": {
        1: "heat",
        2: "cold",
        3: "electrocution",
        4: "acid",
        5: "poison"
    }
}

def roll_table(table, roll=None): 
    if not roll:
        roll = randint(0, len(table) - 1)
    for key in table:
        if roll < key:
            return table[key]
    return None

def populate_flavor(flavor_string, tables):
    while '$' in flavor_string:
        i = flavor_string.find('$')
        tmp = flavor_string[i:]
        i = tmp.find('}')
        tmp = tmp[:i+1]
        word = tmp[2:-1]
        if "number" in word:
            x = int(word.split(':')[1])
            flavor_string = flavor_string.replace(tmp, str(randint(1,x)), 1)
        else:
            if ':' in word:
                word, x = word.split(':')
                flavor_string = flavor_string.replace(tmp, roll_table(tables[word], float(x) if '.' in x else int(x)), 1)
            else:
                flavor_string = flavor_string.replace(tmp, roll_table(tables[word]), 1)
    return flavor_string
