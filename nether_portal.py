def nether_portal(): 
    pos = world.player.pos

    for x in range(4):
        # bottom row
        world.set_block(pos + Direction.EAST * x, Item.OBSIDIAN)
        # top row
        world.set_block(pos + Direction.EAST * x + Direction.UP * 4 , Item.OBSIDIAN)

    for y in range(4):
        # left side
        world.set_block(pos + Direction.UP * y, Item.OBSIDIAN)
        # right side
        world.set_block(pos + Direction.UP * y + Direction.EAST * 3 , Item.OBSIDIAN)

    c = get_client()
    c.give("@a", Item.FLINT_AND_STEEL)

