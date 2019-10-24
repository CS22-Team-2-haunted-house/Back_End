from adventure.models import Player, Room

Room.objects.all().delete()

rooms = [
   {'title': 'The Lobby', 'description': "Quiet, spacious. Whoever owns this place must be rich."},
   {'title': 'The Dining Room', 'description': "Enough to seat at least 100 people, who would need a dining room this big?"},
   {'title': 'The Library', 'description': 'I didn’t know anybody read anymore.'},
   {'title': 'Bedroom 1', 'description': "Blue walls, two cradles, this must be a baby room."},
   {'title': 'The Music room', 'description': "A grand piano sits in the middle of the room, music seems to be playing on its own..."},
   {'title': 'The Study', 'description': "Who needs a study when you already have a library?"},
   {'title': 'The Office', 'description': 'Who needs a library if you already have an office?!'},
   {'title': 'The Kitchen', 'description': "I wonder if they would mind if I cooked something to eat in here..."},
   {'title': 'Bedroom 2', 'description': 'Rather plain, if I had to guess, this would be the guest bedroom.'},
   {'title': 'Bathroom 1', 'description': "Well, I don’t need to use it anymore..."},
   {'title': 'The Gold Ballroom', 'description': "Snow everywhere. There's also a pack of wolves roaming around."},
   {'title': 'The Game Room', 'description': "There’s billiards, darts, but no time to play when I’m already practically playing clue."},
   {'title': 'The Exercise Room', 'description': 'No thanks, I’m practically dripping sweat just by being here.'},
   {'title': 'The Pool Room', 'description': "Didn’t I already see a pool outside when I walked in?"},
   {'title': 'The Hallway', 'description': "I’ve been walking in a straight line for so long it feels like I’m walking in a spiral..."},
   {'title': 'The Armory', 'description': "There’s guns and swords, what would you need all that for?."},
   {'title': 'The Shooting Range', 'description': 'Well, I guess this is where they test out their stuff from the armory.'},
   {'title': 'Bedroom 3', 'description': "Painted bright orange, with a huge bed in the middle of the room and nothing else."},
   {'title': 'The Observatory', 'description': 'Have never been one for sciencey things, myself.'},
   {'title': 'The Green Room', 'description': "These plants are alive, someone has to be around to maintain them."},
   {'title': 'The Pantry', 'description': "A lot of moldy bread, the smell is unbearable."},
   {'title': 'The Drawing Room', 'description': "A blank canvas and an empty chair sits in the middle of the room."},
   {'title': 'The Art Gallery', 'description': 'I wonder who painted these...they’re not very good.'},
   {'title': 'Bathroom 2', 'description': "No thanks, I already went."},
   {'title': 'The Wine Cellar', 'description': "Best not to drink while on the job."},
   {'title': 'Closet 1', 'description': "This closet is about the size of my bedroom at home!"},
   {'title': 'The Master Bedroom', 'description': 'I bet this room is bigger than most peoples homes, I don’t think I’m alone in here.'},
   {'title': 'Bedroom 4', 'description': "White walls, the room is empty but the outlines of where furniture used to be, stain the walls and floor."},
   {'title': 'The Surveillance Room', 'description': 'The first time I’ve seen a screen in this whole house, and this wall is full of them, they’re all just static though.'},
   {'title': 'Closet 2', 'description': "Nothing but towels in here."},
   {'title': 'Bathroom 3', 'description': "This would’ve been useful earlier."},
   {'title': 'The Alphabet Room', 'description': "Christmas lights adorn the wall, under each light is a letter. Strange."},
   {'title': 'The Light Room', 'description': 'I suppose during the day this is where you’d go to see some sun, now its more like The Twilight Zone.'},
   {'title': 'The Laundry Room', 'description': "No washing machine nor dryer, just buckets and washing boards."},
   {'title': 'Closet 3', 'description': "Lots of nice suits and shoes, all hung up and proper, whoever this guy was, he had some taste."},
   {'title': 'The Diorama Room', 'description': "In the middle of the room is a large glass case with a bunch of toy soldiers, looks like it's supposed to be The Great War."},
   {'title': 'The Theater Room', 'description': 'A big screen with a projector in the back, uses good old fashioned film.'},
   {'title': 'The Card Room', 'description': "Nothing in the room except a table with a house of cards in the middle. Odd."},
   {'title': 'The Boxing Room', 'description': 'Another gymnasium, except with a small boxing ring in the middle, gotta get those frustrations out somehow.'},
   {'title': 'The Bird Room', 'description': "An empty room with a small box in the middle, it almost sounds like there's a bird chirping in there."},

   {'title': 'The Lobby(2)', 'description': "Quiet, spacious. Whoever owns this place must be rich.(2)"},
   {'title': 'The Dining Room(2)', 'description': "Enough to seat at least 100 people, who would need a dining room this big?(2)"},
   {'title': 'The Library(2)', 'description': 'I didn’t know anybody read anymore.(2)'},
   {'title': 'Bedroom 1(2)', 'description': "Blue walls, two cradles, this must be a baby room.(2)"},
   {'title': 'The Music room(2)', 'description': "A grand piano sits in the middle of the room, music seems to be playing on its own...(2)"},
   {'title': 'The Study(2)', 'description': "Who needs a study when you already have a library?(2)"},
   {'title': 'The Office(2)', 'description': 'Who needs a library if you already have an office?!(2)'},
   {'title': 'The Kitchen(2)', 'description': "I wonder if they would mind if I cooked something to eat in here...(2)"},
   {'title': 'Bedroom 2(2)', 'description': 'Rather plain, if I had to guess, this would be the guest bedroom.(2)'},
   {'title': 'Bathroom 1(2)', 'description': "Well, I don’t need to use it anymore...(2)"},
   {'title': 'The Gold Ballroom(2)', 'description': "Snow everywhere. There's also a pack of wolves roaming around.(2)"},
   {'title': 'The Game Room(2)', 'description': "There’s billiards, darts, but no time to play when I’m already practically playing clue.(2)"},
   {'title': 'The Exercise Room(2)', 'description': 'No thanks, I’m practically dripping sweat just by being here.(2)'},
   {'title': 'The Pool Room(2)', 'description': "Didn’t I already see a pool outside when I walked in?(2)"},
   {'title': 'The Hallway(2)', 'description': "I’ve been walking in a straight line for so long it feels like I’m walking in a spiral...(2)"},
   {'title': 'The Armory(2)', 'description': "There’s guns and swords, what would you need all that for?.(2)"},
   {'title': 'The Shooting Range(2)', 'description': 'Well, I guess this is where they test out their stuff from the armory.(2)'},
   {'title': 'Bedroom 3(2)', 'description': "Painted bright orange, with a huge bed in the middle of the room and nothing else.(2)"},
   {'title': 'The Observatory(2)', 'description': 'Have never been one for sciencey things, myself.(2)'},
   {'title': 'The Green Room(2)', 'description': "These plants are alive, someone has to be around to maintain them.(2)"},
   {'title': 'The Pantry(2)', 'description': "A lot of moldy bread, the smell is unbearable.(2)"},
   {'title': 'The Drawing Room(2)', 'description': "A blank canvas and an empty chair sits in the middle of the room.(2)"},
   {'title': 'The Art Gallery(2)', 'description': 'I wonder who painted these...they’re not very good.(2)'},
   {'title': 'Bathroom 2(2)', 'description': "No thanks, I already went.(2)"},
   {'title': 'The Wine Cellar(2)', 'description': "Best not to drink while on the job.(2)"},
   {'title': 'Closet 1(2)', 'description': "This closet is about the size of my bedroom at home!(2)"},
   {'title': 'The Master Bedroom(2)', 'description': 'I bet this room is bigger than most peoples homes, I don’t think I’m alone in here.(2)'},
   {'title': 'Bedroom 4(2)', 'description': "White walls, the room is empty but the outlines of where furniture used to be, stain the walls and floor.(2)"},
   {'title': 'The Surveillance Room(2)', 'description': 'The first time I’ve seen a screen in this whole house, and this wall is full of them, they’re all just static though.(2)'},
   {'title': 'Closet 2(2)', 'description': "Nothing but towels in here.(2)"},
   {'title': 'Bathroom 3(2)', 'description': "This would’ve been useful earlier.(2)"},
   {'title': 'The Alphabet Room(2)', 'description': "Christmas lights adorn the wall, under each light is a letter. Strange.(2)"},
   {'title': 'The Light Room(2)', 'description': 'I suppose during the day this is where you’d go to see some sun, now its more like The Twilight Zone.(2)'},
   {'title': 'The Laundry Room(2)', 'description': "No washing machine nor dryer, just buckets and washing boards.(2)"},
   {'title': 'Closet 3(2)', 'description': "Lots of nice suits and shoes, all hung up and proper, whoever this guy was, he had some taste.(2)"},
   {'title': 'The Diorama Room(2)', 'description': "In the middle of the room is a large glass case with a bunch of toy soldiers, looks like it's supposed to be The Great War.(2)"},
   {'title': 'The Theater Room(2)', 'description': 'A big screen with a projector in the back, uses good old fashioned film.(2)'},
   {'title': 'The Card Room(2)', 'description': "Nothing in the room except a table with a house of cards in the middle. Odd.(2)"},
   {'title': 'The Boxing Room(2)', 'description': 'Another gymnasium, except with a small boxing ring in the middle, gotta get those frustrations out somehow.(2)'},
   {'title': 'The Bird Room(2)', 'description': "An empty room with a small box in the middle, it almost sounds like there's a bird chirping in there.(2)"},

   {'title': 'The Lobby(3)', 'description': "Quiet, spacious. Whoever owns this place must be rich.(3)"},
   {'title': 'The Dining Room(3)', 'description': "Enough to seat at least 100 people, who would need a dining room this big?(3)"},
   {'title': 'The Library(3)', 'description': 'I didn’t know anybody read anymore.(3)'},
   {'title': 'Bedroom 1(3)', 'description': "Blue walls, two cradles, this must be a baby room.(3)"},
   {'title': 'The Music room(3)', 'description': "A grand piano sits in the middle of the room, music seems to be playing on its own...(3)"},
   {'title': 'The Study(3)', 'description': "Who needs a study when you already have a library?(3)"},
   {'title': 'The Office(3)', 'description': 'Who needs a library if you already have an office?!(3)'},
   {'title': 'The Kitchen(3)', 'description': "I wonder if they would mind if I cooked something to eat in here...(3)"},
   {'title': 'Bedroom 2(3)', 'description': 'Rather plain, if I had to guess, this would be the guest bedroom.(3)'},
   {'title': 'Bathroom 1(3)', 'description': "Well, I don’t need to use it anymore...(3)"},
   {'title': 'The Gold Ballroom(3)', 'description': "Snow everywhere. There's also a pack of wolves roaming around.(3)"},
   {'title': 'The Game Room(3)', 'description': "There’s billiards, darts, but no time to play when I’m already practically playing clue.(3)"},
   {'title': 'The Exercise Room(3)', 'description': 'No thanks, I’m practically dripping sweat just by being here.(3)'},
   {'title': 'The Pool Room(3)', 'description': "Didn’t I already see a pool outside when I walked in?(3)"},
   {'title': 'The Hallway(3)', 'description': "I’ve been walking in a straight line for so long it feels like I’m walking in a spiral...(3)"},
   {'title': 'The Armory(3)', 'description': "There’s guns and swords, what would you need all that for?.(3)"},
   {'title': 'The Shooting Range(3)', 'description': 'Well, I guess this is where they test out their stuff from the armory.(3)'},
   {'title': 'Bedroom 3(3)', 'description': "Painted bright orange, with a huge bed in the middle of the room and nothing else.(3)"},
   {'title': 'The Observatory(3)', 'description': 'Have never been one for sciencey things, myself.(3)'},
   {'title': 'The Green Room(3)', 'description': "These plants are alive, someone has to be around to maintain them.(3)"},
]

connections = [[0, 1, "e"], [0, 2, "s"], [1, 0, "w"], [1, 10, "e"], [1, 8, "s"], [2, 0, "n"], [2, 3, "s"],
               [3, 2, "n"], [3, 5, "e"], [3, 4, "s"], [4, 3, "n"], [4, 6, "e"], [4, 7, "s"], [5, 3, "w"],
               [5, 9, "e"], [6, 4, "w"], [6, 9, "e"], [7, 4, "w"], [7, 15, "e"], [8, 2, "n"], [8, 12, "e"],
               [8, 9, "s"], [9, 5, "w"], [9, 8, "n"], [9, 6, "s"], [9, 14, "e"], [10, 1, "w"], [10, 12, "s"],
               [10, 11, "e"], [11, 10, "w"], [11, 16, "e"], [12, 8, "w"], [12, 10, "n"], [12, 13, "e"],
               [13, 12, "w"], [13, 14, "s"], [14, 13, "n"], [14, 9, "w"], [14, 15, "s"], [14, 20, "e"],
               [15, 7, "w"], [15, 14, "n"], [15, 22, "s"], [16, 11, "w"], [16, 18, "s"], [16, 17, "e"],
               [17, 16, "w"], [18, 16, "n"], [18, 19, "s"], [19, 18, "n"], [19, 20, "s"], [20, 14, "w"],
               [20, 19, "n"], [20, 23, "e"], [20, 21, "s"], [21, 20, "n"], [21, 22, "s"], [22, 21, "n"],
               [22, 24, "e"], [22, 15, "w"], [23, 20, "w"], [24, 22, "e"], [24, 25, "n"], [25, 26, "w"],
               [25, 27, "e"], [25, 24, "s"], [26, 25, "e"], [27, 25, "w"], [27, 28, "n"], [28, 27, "s"],
               [28, 29, "e"], [29, 28, "w"], [29, 30, "n"],
               
               [30, 31, "s"], [30, 31, "e"], [30, 32, "s"], [31, 30, "w"], [31, 40, "e"], [31, 38, "s"], [32, 30, "n"], [32, 33, "s"],
               [33, 32, "n"], [33, 35, "e"], [33, 34, "s"], [34, 33, "n"], [34, 36, "e"], [34, 37, "s"], [35, 33, "w"],
               [35, 39, "e"], [36, 34, "w"], [36, 39, "e"], [37, 34, "w"], [37, 45, "e"], [38, 32, "n"], [38, 42, "e"],
               [38, 39, "s"], [39, 35, "w"], [39, 38, "n"], [39, 36, "s"], [39, 44, "e"], [40, 31, "w"], [40, 42, "s"],
               [40, 41, "e"], [41, 40, "w"], [41, 46, "e"], [42, 38, "w"], [42, 40, "n"], [42, 43, "e"],
               [43, 42, "w"], [43, 44, "s"], [44, 43, "n"], [44, 39, "w"], [44, 45, "s"], [44, 50, "e"],
               [45, 37, "w"], [45, 44, "n"], [45, 52, "s"], [46, 41, "w"], [46, 48, "s"], [46, 47, "e"],
               [47, 46, "w"], [48, 46, "n"], [48, 49, "s"], [49, 48, "n"], [49, 50, "s"], [50, 44, "w"],
               [50, 49, "n"], [50, 53, "e"], [50, 51, "s"], [51, 50, "n"], [51, 52, "s"], [52, 51, "n"],
               [52, 54, "e"], [52, 45, "w"], [53, 50, "w"], [54, 52, "e"], [54, 55, "n"], [55, 56, "w"],
               [55, 57, "e"], [55, 54, "s"], [56, 55, "e"], [57, 55, "w"], [57, 58, "n"], [58, 57, "s"],
               [58, 59, "e"], [59, 58, "w"], [59, 60, "n"],
               
               [60, 59, "s"], [60, 61, "e"], [60, 62, "s"], [61, 60, "w"], [61, 70, "e"], [61, 68, "s"], [62, 60, "n"], [62, 63, "s"],
               [63, 62, "n"], [63, 65, "e"], [63, 64, "s"], [64, 63, "n"], [64, 66, "e"], [64, 67, "s"], [65, 63, "w"],
               [65, 69, "e"], [66, 64, "w"], [66, 69, "e"], [67, 64, "w"], [67, 75, "e"], [68, 62, "n"], [68, 72, "e"],
               [68, 69, "s"], [69, 65, "w"], [69, 68, "n"], [69, 66, "s"], [69, 74, "e"], [70, 61, "w"], [70, 72, "s"],
               [70, 71, "e"], [71, 70, "w"], [71, 76, "e"], [72, 68, "w"], [72, 70, "n"], [72, 73, "e"],
               [73, 72, "w"], [73, 74, "s"], [74, 73, "n"], [74, 69, "w"], [74, 75, "s"], [74, 80, "e"],
               [75, 67, "w"], [75, 74, "n"], [75, 82, "s"], [76, 71, "w"], [76, 78, "s"], [76, 77, "e"],
               [77, 76, "w"], [78, 76, "n"], [78, 79, "s"], [79, 78, "n"], [79, 80, "s"], [80, 74, "w"],
               [80, 79, "n"], [80, 83, "e"], [80, 81, "s"], [81, 80, "n"], [81, 82, "s"], [82, 81, "n"],
               [82, 84, "e"], [82, 75, "w"], [83, 80, "w"], [84, 82, "e"], [84, 85, "n"], [85, 86, "w"],
               [85, 87, "e"], [85, 84, "s"], [86, 85, "e"], [87, 85, "w"], [87, 88, "n"], [88, 87, "s"],
               [88, 89, "e"], [89, 88, "w"], [89, 90, "n"],
               
               [90, 89, "s"], [90, 91, "e"], [90, 92, "s"], [91, 90, "w"], [91, 100, "e"], [91, 98, "s"], [92, 90, "n"], [92, 93, "s"],
               [93, 92, "n"], [93, 95, "e"], [93, 94, "s"], [94, 93, "n"], [94, 96, "e"], [94, 97, "s"], [95, 93, "w"],
               [95, 99, "e"], [96, 94, "w"], [96, 99, "e"], [97, 94, "w"], [98, 92, "n"], [98, 12, "e"],
               [98, 99, "s"], [99, 95, "w"], [99, 98, "n"], [99, 96, "s"], [100, 91, "w"]]

saved_rooms = []

for i in range(len(rooms)):
    saved_rooms.append(Room(title=rooms[i]['title'], description=rooms[i]['description']))
    saved_rooms[i].save()

for i in range(len(connections)):
    saved_rooms[connections[i][0]].connect_rooms(saved_rooms[connections[i][1]], connections[i][2])

players = Player.objects.all()
for p in players:
    p.currentRoom = saved_rooms[0].id
    p.save()
