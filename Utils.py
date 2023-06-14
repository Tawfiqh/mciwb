
class Utils:

    def __init__(self, world, username):
        self.world = world
        self.username=username
        self.world.cmd(f"/op {self.username}")

    def run_command(self, cmd_str):
        print(cmd_str)
        self.world.cmd(cmd_str)

    def random_move(self, raduis_from_origin = 1000):
        import random

        def rand_dist(upper=raduis_from_origin):
            return random.randint(1, upper)

        def get_random_position():
            high_height = rand_dist(100)
            position = Vec3(x=rand_dist(), y=high_height, z=-rand_dist())
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
        
        self.run_command(f"/tp {self.username} {new_player_position.x} {new_player_position.y} {new_player_position.z}")
    
    def clear_weather(self):
        self.world.cmd("/weather clear")
        
    def clear_time(self):
        self.world.cmd("/time set 0")
    
    def reset_time_and_weather(self):
        self.clear_weather()
        self.clear_time()
       

u = Utils(world, "tawfiqh")
u.random_move()