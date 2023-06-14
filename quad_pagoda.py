class PagodaBuilder:
    def __init__(self, player_pos):
        # Constructor (optional)
        self.player_pos = player_pos


    def auto_build_pagodas_around_player(self, offset_int = 20):
        player_pos = self.player_pos
        def build_pagoda(pos, width=4, floor_height=4, item: Item = Item.GOLD_BLOCK):
            """
            Create a pagoda out of blocks at the given position.

            Each successive floor is narrower and each has a balcony at the top.

            :param pos: position of the base of the pagoda
            :param width: width of the base of the pagoda
            :param floor_height: height of each floor
            :param item: block to use for the base of the pagoda
            """
            c = get_client()

            # calculate how many levels we can make if we reduce width by 2 each level
            levels = width // 2

            for level in range(levels):
                # calculate the width of the pagoda for this level
                floor_width = width - 2 * level

                # calculate the base position of the walls for this level
                base = pos + Direction.UP * level * floor_height

                # calculate the position of the balcony for this level
                # it should surround the top layer of the walls for this level
                balcony = base + Direction.UP * (floor_height - 1)

                # create the balcony for this level
                polygon(
                    client=c,
                    center=balcony,
                    height=1,
                    diameter=floor_width + 2,
                    sides=4,
                    item=item,
                    mode=FillMode.REPLACE,
                )

                # create the walls for this level
                polygon(
                    client=c,
                    center=base,
                    height=floor_height,
                    diameter=floor_width,
                    sides=4,
                    item=item,
                    mode=FillMode.REPLACE,
                )


        def build_pagoda_at_offset_from_player(offset_x=0, offset_y=0, offset_z=0, player_pos=player_pos):
            pagoda_pos=Vec3(offset_x, offset_y, offset_z)
            build_pagoda(player_pos + pagoda_pos, width=10)

        build_pagoda_at_offset_from_player(offset_int,0, offset_int)
        build_pagoda_at_offset_from_player(offset_int, 0, offset_int * -1)
        build_pagoda_at_offset_from_player(offset_int * -1, 0, offset_int)
        build_pagoda_at_offset_from_player(offset_int * -1, 0, offset_int * -1)


pb = PagodaBuilder(world.player.pos)
pb.auto_build_pagodas_around_player()