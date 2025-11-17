#Start
import random

#Story
print("The game starts with you waking up on the floor infront of 3 doors.")
print("You have no idea what this place is or how you got there.")
print("But you do know that it is not smart to stay still for long.")

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
        
        
class Item():
    def __init__(self):
        self.items = ["Sword", "Bandage", "Axe", "Potion"] # List of items

    def chest(self):
        item = random.choice(self.items)
        substat = random.randint(1, 101) # OBS: FIX THE RARITY SYSTEM
        
        return item, 1

    def inventory():
        print("PLACEHOLDER") # Adding this later
        
        


adventurer = Adventurer()
print(f"Welcome to the Hall of Beasts, {adventurer.name}")

#Randomizing results
contents = ["Monster", "Chest", "Trap"]

# While Loop
while True:    
    door_choice = input("""
Which door do you want to enter?"            
[A] Door 1 (To the left)
[B] Door 2 (Forward)
[C] Door 3 (To the right)
> """).lower()

    door_choice_result = random.choice(contents)

    if door_choice == "a":
        print(f"You open door 1 and found a {door_choice_result}!")
            
    elif door_choice == "b":
        print(f"You open door 2 and found a {door_choice_result}!")

    elif door_choice == "c":
        print(f"You open door 3 and found a {door_choice_result}!")

    else:
        print("ERROR! Invalid input please try again.")
        continue
    
    #Dumb ways to die 
    if door_choice_result == "Trap":
        print("You stepped on a trap and took 1 points of damage")
        adventurer.trap(1)          

    elif door_choice_result == "Chest":
        print("You opened the chest and found howard gaming!")
        adventurer.chest(Item.chest())
    
    elif door_choice_result == "Monster":
        print("Oh,no! A very large and intimidating monster has appeared. You better prepare for battle!")
        if adventurer.properties > #insert monster properties
            print("You defeated the monster and leveled up!")
        elif adventurer.properties < #insert monster properties
            print("The monster posseses unimaginable strength and overpowers you!") 
            adventurer.monster(1)
        elif adventurer.properties == #insert monster properties 
            print("You both posses the same level of strength causing a stalemate!")
        
    else:
        print("ERROR! Invalid input please try again.") 
        continue   
    



    