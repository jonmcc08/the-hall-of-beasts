#Start
import random
import time # For dialouge delays (Printing is slower)

# Classes

class Adventurer(): # Instead of calling the class "Player", we call it Adventurer
    # Defines the Adventurers name and creates the properties of the player.
    def __init__(self):
        self.name = input("""Enter the adventurers name.
> """).upper()
        self.inventory = {} # Showcases possesed items.
        self.properties = [5, 1, 0] # Includes in following order: 5 HP, 1 STR, 0 LVL.

    def monster(self, monster):
        self.properties[0] -= monster
        print(f"You have {self.properties[0]} HP left")

    def trap(self, trap):
        self.properties[0] -= trap
        print(f"You have {self.properties[0]} HP left")

    def chest(self, item, stat):
        self.inventory[item] = stat
        print(self.inventory) # TESTING PURPOSES

    def strenght(self, str_increase):
        self.properties[1] += str_increase
        
class Final_boss(): 
    def __init__(self):
        self.name = "Hugo Beast"
        self.properties = [100, 1, 100]
        
        
class Item():
    
    def __init__(self):
        self.items = ["Sword", "Bandage", "Axe", "Potion"] # List of items

    def chest(self):
        item = random.choice(self.items)
        substat = random.randint(1, 101) 

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
        
        return item, rarity # FIx

    def inventory():
        pass


        
class monster():
    def __init__(self):
        self.strength = random.randint(1,10)


def story_printing(string, seconds):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(seconds)
    print()

#Story
story_printing("The game starts with you waking up on the floor infront of 3 doors.", 0.07)
story_printing("You have no idea what this place is or how you got here. ", 0.07)
story_printing("But you do know that it is not smart to stay still for long.", 0.07)
print()

adventurer = Adventurer()
item = Item()
final_boss = Final_boss()

story_printing(f"Welcome to the Hall of Beasts, {adventurer.name}", 0.1)

#Randomizing results
contents = ["Monster", "Chest", "Trap"]

# While Loop
while True:    
    door_choice = input("""
Which door do you want to enter?           
[A] Door 1 (To the left)
[B] Door 2 (Forward)
[C] Door 3 (To the right)
[D] See adventurer stats
[E] See adventurer inventory
> """).lower()

    door_choice_result = random.choice(contents)

    if door_choice == "a":
        print(f"You open door 1 and found a {door_choice_result}!")
            
    elif door_choice == "b":
        print(f"You open door 2 and found a {door_choice_result}!")

    elif door_choice == "c":
        print(f"You open door 3 and found a {door_choice_result}!")

    elif door_choice == "d":
        print(f"You take a look at your current strength {adventurer.properties}")
        continue
    
    elif door_choice == "e":
        print(f"You take a look at your items")    
        continue
    
    else:
        print("ERROR! Invalid input please try again.")
        continue
    
    #Dumb ways to die 
    if door_choice_result == "Trap":
        print("You stepped on a trap and took 1 points of damage")
        adventurer.trap(1)          

    elif door_choice_result == "Chest":
        recieved_item = list(item.chest()) # FIX
        adventurer.chest(recieved_item) # FIX THIS ISSUE
        print(f"You opened the chest and a {recieved_item[0]} with a rarity of: {recieved_item[1]}")
        
    elif door_choice_result == "Monster":
        print("Oh,no! A very large and intimidating monster has appeared. You better prepare for battle!")
        if adventurer.properties[1] > 1: #insert monster properties
            print("You defeated the monster and leveled up!")
        elif adventurer.properties[1] < 1: #insert monster properties
            print("The monster posseses unimaginable strength and overpowers you!") 
            adventurer.monster(1)
        elif adventurer.properties[1] == 1: #insert monster properties 
            print("You both posses the same level of strength causing a stalemate!")
        
    else:
        print("ERROR! Invalid input please try again.") 
        continue 
    
    if adventurer.properties[2] == 9: # When adventurers level is 9, the loop ends and you enter the final phase of the game.
        break 

#Final Boss dialouge
story_printing(f"You come to me with bad intentions {adventurer.name}", 0.07)
story_printing("You may have gotten passed my minions, but I'll be your undoing!", 0.07)
story_printing("You came to fight? Let's see what you got!", 0.1)

while final_boss.properties[1] > 0:
    pass