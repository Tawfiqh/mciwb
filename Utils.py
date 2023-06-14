
class Utils:

    def __init__(self, world, username):
        self.world = world
        self.username=username
        self.world.cmd(f"/op {self.username}")

    def run_command(self, cmd_str):
        print(cmd_str)
        self.world.cmd(cmd_str)

    def get_random_teleport_destination(self, radius_from_origin = 1000):
        import random

        def rand_dist(upper=radius_from_origin):
            return random.randint(1, upper)

        def get_random_position():
            high_height = rand_dist(100)
            position = Vec3(x=rand_dist(), y=high_height, z=rand_dist())
            return position
        
        def check_position_is_air(position):
            try:
                print(f"Checking: {position}")
                block_to_check = self.world.get_block(position)
            except ValueError:
                return False
            
            # Check if the block is air
            return block_to_check == Item.AIR
        
        new_player_position = get_random_position()
        while check_position_is_air(new_player_position) != True:
            new_player_position = get_random_position()
        return new_player_position

    def random_teleport(self, radius_from_origin = 1000):
        new_player_position = self.get_random_teleport_destination(radius_from_origin)
        self.run_command(f"/tp {self.username} {new_player_position.x} {new_player_position.y} {new_player_position.z}")
    

    def random_teleport_block_by_block(self,radius_from_origin=1000):
        from math import sqrt

        original_pos = self.world.player.pos
        new_pos = self.get_random_teleport_destination(radius_from_origin)


        distance = sqrt((new_pos.x - original_pos.x) ** 2 + (new_pos.y - original_pos.y) ** 2 + (new_pos.z - original_pos.z) ** 2)

        def normalize(vector):
            magnitude = sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)
            return Vec3(vector.x / magnitude, vector.y / magnitude, vector.z / magnitude)

        # Calculate the unit vector between the two vectors
        unit_vector = normalize(new_pos - original_pos)

        # Move along the vector between the two vectors in increments of 10
        for i in range(0, int(distance)):
            interim_pos = original_pos + unit_vector * i
            self.run_command(f"/tp {self.username} {interim_pos.x} {interim_pos.y} {interim_pos.z}")

    def keep_travelling(self, distance=1000, iterations=10):
        for i in range(iterations):
            self.random_teleport_block_by_block(distance)

    def clear_weather(self):
        self.world.cmd("/weather clear")
        
    def clear_time(self):
        self.world.cmd("/time set 0")
    
    def reset_time_and_weather(self):
        self.clear_weather()
        self.clear_time()
       

u = Utils(world, "tawfiqh")
u.random_teleport_block_by_block(1000)
u.keep_travelling()