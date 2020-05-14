#intro
intro = "Welcome to THE Game. This is a simple adventure game where you can explore the ingame mansion, collect items, and use them to interact with characters. The goal is to get out of the strange place you woke up in. \nHow to play: \nGame is proceeding by you typing commands into command line. Commands available: \nMove to direction: 'south', 'north', 'west', 'east' \nTake an item from the room: 'take item_name' \nTalk to character: 'talk' \nFight a character: 'fight' \nInspect the room closely: 'inspect' \nCheck your backpak: 'backpack' \n"

#ending

ending = "Congratulations with getting out of this place. You are free now."

#rooms

kitchen_name = "Kitchen"
kitchen_description = "A dank and dirty room buzzing with flies."
kitchen_inspect = "Looks completely abandoned, except for the big piece of nice looking Cheese on the table. Flies avoid it for some reason."

dining_hall_name = "Dining Hall"
dining_hall_description = "About twice as big as kitchen, with big table in the middle and some scattered chairs. looks completely abandoned."
dining_hall_inspect = "Nothing of value can be found here. Only dust and damaged furniture"

ballroom_name = "Ballroom"
ballroom_description = "Big room with an even bigger window, which hasn't been washed for a long time, fills room  with grey light."
ballroom_inspect = "Looks like someone took everything out of this room"

#characters

dave_name = "Dave"
dave_description = "A smelly zombie"
dave_conversation = "BRRRRRAAAAINS"
dave_weakness = "Cheese"

elsa_name = "Elsa"
elsa_description = "Little girl"
elsa_conversation = "What are you doing here?"
elsa_possession = "Tiara"
elsa_treat = "Candy"

#items

cheese_name = 'Cheese'
cheese_description = 'Big and smelly piece of cheese. Can be used as weapon'
cheese_charges = 1
cheese_usage = f'Restores one heart. Can be used {cheese_charges} times'

candy_name = 'Candy'
candy_description = 'Liked by kids'
candy_charges = 1
candy_usage = f'Restores half a heart. Can be used {candy_charges} times'

tiara_name = 'Tiara'
tiara_description = 'Silver tiara with glowing gemstome in the center of it'
tiara_usage = 'Grants night vision'

nightshirt_name = 'Nightshirt'