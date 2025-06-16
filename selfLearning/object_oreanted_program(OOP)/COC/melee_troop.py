from troop import Troop

class MeleeTroop(Troop):
    
    def __init__(self, name, hitpoint, level, damage, death_damage, moment_speed, 
                 training_time, housing_space, training_cost, troop_range,attack_speed,
                 target_type, area_damage, favorite_building= "None", troop_type= "Ground",
                    damage_type= "single"):
        super().__init__(name, hitpoint, level, damage, death_damage, moment_speed,
                         training_time, housing_space, training_cost, troop_range,
                         favorite_building, troop_type, damage_type, attack_speed,
                         target_type)
        self.area_damage = area_damage
        self.ishero = False 
        self.ismelee = True

    def __str__(self):
        pass
