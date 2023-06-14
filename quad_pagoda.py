class PagodaBuilder:
    def __init__(self, player_pos):
        # Constructor (optional)
        self.player_pos = player_pos

    # List of materials here: https://github.com/conqp/mcipc/blob/master/mcipc/rcon/item.py
    def make_castle(self, offset = 20, material=Item.GOLD_BLOCK):
        player_pos = self.player_pos
        def build_pagoda(pos, width=4, floor_height=4, item: Item = material):
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


        def pagoda_at_offset_from_player(offset_x=0, offset_y=0, offset_z=0, player_pos=player_pos, width=10):
            pagoda_pos=Vec3(offset_x, offset_y, offset_z)
            build_pagoda(player_pos + pagoda_pos, width=width)

        pagoda_at_offset_from_player(offset,0, offset)
        pagoda_at_offset_from_player(offset, 0, offset * -1)
        pagoda_at_offset_from_player(offset * -1, 0, offset)
        pagoda_at_offset_from_player(offset * -1, 0, offset * -1)
        pagoda_at_offset_from_player(offset * -1, 0, offset * -1)
        pagoda_at_offset_from_player(width=30)




pb = PagodaBuilder(world.player.pos)
pb.make_castle(material=Item.DIAMOND_BLOCK)
