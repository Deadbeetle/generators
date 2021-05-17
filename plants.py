from random import random, randint
import common

tables = {
    "descriptors": {
        1: "woody",
        2: "flowering",
        3: "sprawling",
        4: "climbing"
    },
    
    "parts": {
        1: "stems",
        2: "leaves", 
        3: "fruits",
        4: "thorns",
        5: "flowers",
        6: "roots",
        7: "seeds"
    },
    
    "tastes": {
        1: "sweet",
        2: "sour",
        3: "bitter",
        4: "salty",
        5: "savory"
    },
    
    "smells": {
        1: "sweet",
        2: "putrid",
        3: "sulfurous",
        4: "like mold"
    },
    
    "textures": {
        1: "soft",
        2: "juicy",
        3: "tough",
        4: "crunchy"
    },
    
    "preparations": {
        1: "eaten",
        2: "made into a jelly",
        3: "dried and ground into a powder",
        4: "crushed into a paste",
        5: "boiled"
    },
    
    "flavor": {
        1: "1It only blooms once every ${number:10} years",
        2: "0Its ${parts} turn ${colors} when the soil has ${soil_properties}",
        3: "0The ${parts} can be ${usages}",
        4: "0The ${parts} are ${textures} and taste ${tastes} when ${preparations}",
        5: "0A certain pathogen will cause the ${parts} to ${minor_symptoms} before eventually ${major_symptoms}",
        6: "0The ${parts} are edible and high in ${nutrients}",
        7: "0The ${parts} are edible, but nutritionally poor",
        8: "0The ${parts} smell ${smells}",
        9: "2It blooms in ${seasons}"
    },
    
    "minor_symptoms": {
        1: "turn ${colors}",
        2: "develop ${colors} spots",
        3: "shrivel up",
        4: "grow irregularly"
    },
    
    "major_symptoms": {
        1: "liquefying",
        2: "exploding",
        3: "falling off",
        4: "rotting in place",
        5: "killing the whole plant"
    },
    
    "soil_properties": {
        1: "high pH",
        2: "low pH",
        3: "high concentrations of ${minerals}",
        4: "a deficiency in ${elements}"
    },
    
    "elements": {
        1: "nitrogen",
        2: "phosphorus",
        3: "potassium",
        4: "calcium",
        5: "sulfur",
        6: "magnesium"
    },
    
    "minerals": {
        1: "iron",
        2: "copper",
        3: "mythril",
        4: "adamantine",
        5: "calcium",
        6: "zinc",
        7: "nickel"
    },
    
    "nutrients": {
        1: "fiber",
        2: "protein",
        3: "sugar",
        4: "carbohydrates",
        5: "fat"
    },
    
    "effects": {
        1: "treat ${symptoms}",
        2: "cause ${symptoms}",
        3: "cause ${symptoms} and ${symptoms}",
        4: "grant temporary ${boons}"
    },
    
    "products": {
        1: "a tea",
        2: "an ointment",
        3: "a potion"
    },
    
    "usages": {
        1: "used to make ${products} that can ${effects}",
        2: "applied topically to ${effects}",
        3: "eaten to ${effects}",
        4: "burned and the smoke inhaled to ${effects}",
        5: "distilled and injected to ${effects}"
    },
    
    **common.tables
}



class Plant:
    def __init__(self):
        self.size = random()*randint(1,10)*randint(1,10)
        self.appearance = common.populate_flavor("A ${sizes:%.2f} (%.2f ft), ${descriptors} plant with ${colors} ${parts} and ${colors} ${parts}" % (self.size, self.size), tables)
        self.flavor = list()
        temp = ''
        hold = ''
        track = 0
        for i in range(randint(1,10)+2):
            while track != 1:
                temp = common.populate_flavor("${flavor}", tables)
                if temp[0] not in hold or temp[0] == '0':
                    hold = hold + temp[0]
                    temp = temp[1:]
                    self.flavor.append(temp)
                    temp = ''
                    track = 1
            track = 0
    def __str__(self):
        return "{}.".format(".\n".join([self.appearance, *self.flavor]))
