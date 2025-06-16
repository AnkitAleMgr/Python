from troop import Troop

class RangeTroop(Troop):

    def __init__(self, name, hitpoint, level, damage, death_damage, moment_speed,
                 training_time, housing_space, training_cost, troop_range, attack_speed,
                 target_type,area_damage, favorite_building= "None", troop_type = "Ground", damage_type = "Single"):
        super().__init__(name, hitpoint, level, damage, death_damage, moment_speed, training_cost, training_time,
                         housing_space, training_cost, troop_range, attack_speed, target_type, favorite_building,
                         troop_type,damage_type)
        self.area_damage = area_damage
        self.is_hero = False
        self.is_range = True