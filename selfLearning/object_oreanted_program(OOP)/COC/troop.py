from game_object import GameObject

class roop(GameObject):  

    def __init__ (self, name, hitpoint, level, damage, death_damage, moment_speed, 
                  training_time, housing_space, training_cost, troop_range,attack_speed,target_type, 
                  favorite_building= "None", troop_type= "Ground" , damage_type= "single"):
        super().__init__(name, hitpoint, level)
        self.damage = damage
        self.moment_speed = moment_speed
        self.favorite_building = favorite_building
        self.type = troop_type
        self.training_time = training_time
        self.housing_space = housing_space
        self.attack_speed = attack_speed
        self.damage_type = damage_type
        self.target_type = target_type
    
        self.training_cost = training_cost
        self.troop_range = troop_range
        self.death_damage = death_damage


    def __str__(self ):
        pass