from game_object import GameObject

class Building(GameObject):
    
    def __init__(self, name, hitpoint, level, building_time, building_cost, upgrade_cost, upgrade_time, size):
        super().__init__(name, hitpoint, level)
        self.building_time = building_time
        self.building_cost = building_cost
        self.size = size
        self.upgrade_cost = upgrade_cost
        self.upgrade_time = upgrade_time


    def __str__(self):
        pass

