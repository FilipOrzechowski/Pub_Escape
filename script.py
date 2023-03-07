from graph import create_graph
from objects import Map_Objects

rules = input("Welcome to the game \"Pub Escape\"!!!\nIf you want to read the rules, press \"Y\", if you know the rules and want to start playing, press enter. ").upper()
if rules == "Y":
    input("While you're enjoying a nice time at the pub, sipping beer from a mug and flirting with the beautiful bartender, suddenly you notice that someone is watching you.\nIt turns out to be her possessive boyfriend, who looks nervous about your conversation and quickly starts heading towards you.\nSince he is like an angry rhino, it's better not to wait for him to approach you, but to run out of the pub.\nPress enter to continue...")
    input("To successfully complete the game, you must reach the exit before the angry bartender's boyfriend catches you.\nTables are an obstacle that you must avoid while escaping, but at the same time you can use them confuse your pursuer.\nPress enter to continue...")
    print("The legend below shows the keys used to select the direction you want to move your character:")
    input("w - up\ne - upper right\nd - right\nc - lower right\nx - down\nz - lower left\na - left\nq - upper left\ns - stay in the same place\nPress enter to continue...")
    input("The legend below shows the markings of objects on the map:\nX - table\n@ - angry boyfriend\n* - you\nPress enter to start the game...")

map_size = input("Select map size:\n\"S\" for small\n\"M\" for medium\n\"L\" for large ").upper()
while map_size not in ["S", "M", "L"]:
    map_size = input("Wrong letter, try again. ").upper()

if map_size == "S":
    dimention = 8

elif map_size == "M":
    dimention = 10

elif map_size == "L":
    dimention = 12

pub = Map_Objects(create_graph, dimention)
pub.create_complete_map()
while pub.player != pub.enemy and pub.player != pub.exit:
    pub.change_player_position()
    pub.print_map()
    pub.change_enemy_position()
    pub.print_map()

if pub.player == pub.enemy:
    input("You couldn't escape and the barmaid's boyfriend got you...")
    print("...luckily your power of persuasion allowed you to befriend him and spend the rest of the evening together telling stories over a pint of beer.")

if pub.player == pub.exit:
    print("You managed to escape. The whole situation made you think that instead of going to pubs you could spend more time learning Python.")
