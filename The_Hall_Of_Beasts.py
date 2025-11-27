#Start
import random
import time # For dialouge delays (Printing slower)

# Classes

class Adventurer(): # Instead of calling the class "Player", we call it Adventurer
    # Defines the Adventurers name and creates the properties of the player.
    def __init__(self):
        self.name = input("""Enter the adventurers name. \n> """).upper()
        self.inventory = {} # Showcases possesed items.
        self.properties = [5, 1, 0] # Includes in following order: 5 HP, 1 STR, 0 LVL.

    def monster(self, monster):
        if monster == 1:
            self.properties[0] -= 1
            print(f"You have {self.properties[0]} HP left")
        else:
            self.properties[2] += 1

    def trap(self, trap):
        self.properties[0] -= trap
        print(f"You have {self.properties[0]} HP left")

    def chest(self, found_item, stat):
        self.inventory[found_item + str(item.item_ID)] = stat 
        print(self.inventory) # TESTING PURPOSES

    def strenght(self, str_increase):
        self.properties[1] += str_increase
        
class Final_boss(): 
    def __init__(self):
        self.name = "Hugo Beast"
        self.properties = [100, 1, 100]
        
        
class Item():
    
    def __init__(self):
        self.items = ["Sword", "Axe", "Potion"] # List of items
        self.item_ID = 0

    def chest(self):
        item = random.choice(self.items)
        substat = random.randint(1, 101) 
        self.item_ID += 1

        if substat == 1:
            rarity = "Legendary | + 4 STR"
            adventurer.strenght(4)
        elif 1 < substat <= 10:
            rarity = "Epic | + 3 STR"
            adventurer.strenght(3)
        elif 10 < substat <= 40:
            rarity = "Uncommon | + 2 STR"
            adventurer.strenght(2)
        else:
            rarity = "Common | + 1 STR"
            adventurer.strenght(1)
        
        return item, rarity

    def inventory(self):
        i = 1
        for item_ID_inventory in adventurer.inventory.keys():
            current_item = ""
            for char in item_ID_inventory:
                if char.isalpha():
                    current_item += char
                else:
                    break
            print(f"{i}. {current_item}: {adventurer.inventory[item_ID_inventory]}")
            i += 1
        pass

def monster_hp_calculation():
    health = random.randint((-5 + adventurer.properties[1]), (2 + adventurer.properties[1])) # Keeping the chances the same
    return health

def story_printing(string, seconds):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(seconds)
    print()

# Story
story_printing("The game starts with you waking up on the floor infront of 3 doors.", 0.07)
story_printing("You have no idea what this place is or how you got here. ", 0.07)
story_printing("But you do know that it is not smart to stay still for long.", 0.07)
print()

adventurer = Adventurer()
item = Item()
final_boss = Final_boss()
contents = ["Monster", "Chest", "Trap"]

story_printing(f"Welcome to the Hall of Beasts, {adventurer.name}", 0.1)


# While Loop
while True:    
    door_choice = input("""What's your choice?\n[A] Door 1 (To the left)\n[B] Door 2 (Forward)\n[C] Door 3 (To the right)\n[D] See adventurer stats\n[E] See adventurer inventory\n> """).lower()

    door_choice_result = random.choice(contents)

    if door_choice == "a":
        print(f"You open door 1 and found a {door_choice_result}!")
            
    elif door_choice == "b":
        print(f"You open door 2 and found a {door_choice_result}!")

    elif door_choice == "c":
        print(f"You open door 3 and found a {door_choice_result}!")

    elif door_choice == "d":
        print(f"""Current HP: {adventurer.properties[0]}\nCurrent STR: {adventurer.properties[1]}\nCurrent LVL: {adventurer.properties[2]}""")
        continue
    
    elif door_choice == "e":
        item.inventory()
        continue
    
    else:
        print("ERROR! Invalid input please try again.")
        continue
    
    #Dumb ways to die 
    if door_choice_result == "Trap":
        print("You stepped on a trap and took 1 points of damage")
        adventurer.trap(1)          

    elif door_choice_result == "Chest":
        recieved_item, recieved_stat = (item.chest())
        adventurer.chest(recieved_item, recieved_stat)
        print(f"You opened the chest and found a {recieved_item} with a rarity of: {recieved_stat}")
        
    elif door_choice_result == "Monster":
        print("Oh,no! A very large and intimidating monster has appeared. You better prepare for battle!")
        monster_health = monster_hp_calculation()
        if adventurer.properties[1] > monster_health: #insert monster properties
            print("You defeated the monster and leveled up!")
            adventurer.monster(0)
        elif adventurer.properties[1] < monster_health: #insert monster properties
            print("The monster posseses unimaginable strength and overpowers you!") 
            adventurer.monster(1)
        elif adventurer.properties[1] == monster_health: #insert monster properties 
            print("You both posses the same level of strength causing a stalemate!")
        
    else:
        print("ERROR! Invalid input please try again.") 
        continue 
    
    if adventurer.properties[2] == 9: # When adventurers level is 9, the loop ends and you enter the final phase of the game.
        break 

#Final Boss dialouge
story_printing(f"You come to me with bad intentions {adventurer.name}", 0.07)
story_printing(f"You may have gotten passed my minions {adventurer.name}, but I'll be your undoing!", 0.07)
story_printing("You came to fight? Let's see what you got!", 0.1)

#BOSS fight !
while final_boss.properties[0] > 0:
    BOSS_fight_action = input("""What will you do?\n[A] Fight!\n[B] Block!\n[C] Dodge!\n[D] Drink potion!\n> """).lower()
    
    #Actions
    if BOSS_fight_action =="a":
        print("You slash Hugo Beast with all you're might !")
        {final_boss.properties} - {adventurer.properties[1]} 
        
    elif BOSS_fight_action =="b":
        Block_ods = random.randint(1,101)
        if Block_ods == range(1,51):
            print("You managed to block the Beasts attack")
            print("Hugo became stunned")        
    
    elif BOSS_fight_action =="c":
        Dodge_ods = random.randint(1,101)
        if Dodge_ods == range(1,71):
            print("You manage to dodge the Beasts attack")

    elif BOSS_fight_action == "d":
        if item.potion >= 1:
            adventurer.property[0] += 1
            print("You drank a potion and gained HP")
            print(f"You now have {adventurer.properties[0]} HP")
            continue
        elif item.potion < 1:
            print("oh,no! You have no more potion. You have to make another choice")
            continue
