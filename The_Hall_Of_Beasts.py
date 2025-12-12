#Start
import random
import time # For dialouge delays (Printing slower)

# Classes

class Adventurer(): # Instead of calling the class "Player", we call it Adventurer
    # Defines the Adventurers name and creates the properties of the player.
    def __init__(self):
        self.name = input("""Enter the adventurers name. \n> """).upper()
        self.inventory = {} # Showcases possesed items.
        self.potions = {}
        self.properties = [5, 1, 0] # Includes in following order: 5 HP, 1 STR, 0 LVL.

    def monster(self, hp):

        print("a very large and intimidating monster. You better prepare for battle!")
        time.sleep(1)
        if self.properties[1] > hp:
            self.properties[2] += 1
            print(f"You defeated the monster and leveled up! \nYou are now LVL: {self.properties[2]}\n")
        elif self.properties[1] < hp:
            self.properties[0] -= 1
            print(f"The monster posseses unimaginable strength and overpowers you! \nYou now have {self.properties[0]} HP left.\n")
        elif self.properties[1] == hp:
            print("You both posses the same level of strength causing a stalemate!\nNothing happens.\n")

    def trap(self, trap):
        self.properties[0] -= trap
        print(f"a trap and took 1 points of damage \n You now have {self.properties[0]} HP left.\n")

    def chest(self, found_item, stat):
        self.inventory[found_item + str(item.item_ID)] = stat 

    def strenght(self, str_increase):
        self.properties[1] += str_increase
    
    def potion(self, found_item, stat):
        self.potions[found_item + str(item.item_ID)] = stat

    def inventory_full(self, item_choice):
        while True:
            choice = input(f"Your inventory is full, please decide on if you want to replace an item with {item_choice} or discard it (Discard/Replace)\n>").lower()
            if choice.startswith("r"):
                while True:
                    print("Which of the follow items do you want to discard?")
                    item.inventory()
                    item_list = []
                    for item_in_inventory in self.inventory.keys():
                        item_list.append(item_in_inventory)
                    try:
                        chosen_item = (int(input("> ")) - 1)
                        if 1 <= chosen_item <= 5:
                            print(f"You removed the item: {item_list(chosen_item)}: {self.inventory[item_list(chosen_item)]}")
                            self.inventory.pop(item_list[(chosen_item)])
                            break
                    except ValueError:
                        print("ERROR! Invalid input, please try again.")
                        # PROBLEM HÄR UPPE: MÅSTE FIXAS
                break
            elif choice.startswith("d"):
                print("You discared the item.")
                break
            else:
                print("ERROR! Invalid input, please try again.")

class Stunned_effect():
    def __innit__(self):
        self.duration = 0

    def apply_effect_boss():
        Final_boss.stunned = True

    def start_effect(self):
        self.duration = 2
        self.active = True

    def reduce_effect_boss(self):
        self.duration -= 1
        if self.duration <= 0:
            Final_boss.stunned = False
            print("Hugo is no longer stunned!")
        else:
             print(f"Effect duration remaining: {self.duration} turn(s).")

class Final_boss(): 
    def __init__(self):
        self.name = "Hugo Beast"
        self.properties = [20,100] # HP,LVL
        self.stunned = False

    def damage(self, ods):
        
        print("You slash Hugo Beast with all your might!")
        time.sleep(1)
        
        if self.stunned == True:
            self.properties[0] - adventurer.properties[1]
            print(f"Hugo Beast was stunned and thus you managed to hurt him. His current health is {self.properties[0]}.")
        elif final_boss.stunned == False:
            if ods == 1 <= 30:
                print("Hugo Beast repelled your attack, you did 0 damage.")
            else:
                self.properties[0] - adventurer.properties[1]
    
    def stunned(self, ods):
        
        if ods == 1 <= 71:
            self.stunned = True
            print("You managed to block the Beasts attack. \nHugo became stunned")
        else:
            adventurer.properties[0] -= 1
            print(f"You were overwhelemed by the Beasts strength and took 1 points of damage.\nCurrent HP {adventurer.properties[0]}.")

    def dodge(self, ods):
        if ods == 1 <= 81:
            print("You manage to dodge the Beasts attack")                  
        else:
            adventurer.properties[0] -= 1
            print(f"You failed to dodge the attack.\n You take 1 points of damage.\n Current HP {adventurer.properties[0]}.")


class Item():
    
    def __init__(self):
        self.items = ["Sword", "Axe", "Potion", "Daggers", "Knife"] # List of items
        self.item_ID = 0

    def chest(self):
        item_choice = random.choice(self.items)
        substat = random.randint(1, 101) 
        self.item_ID += 1
        
        if item_choice == "Potion":
            item_type = "HP"
        else:
            item_type = "STR"
        
        if substat == 1:
            rarity = f"Legendary | + 4 {item_type}"
            item_strenght = 4
        elif 1 < substat <= 10:
            rarity = f"Epic | + 3 {item_type}"
            item_strenght = 3
        elif 10 < substat <= 40:
            rarity = f"Uncommon | + 2 {item_type}"
            item_strenght = 2
        else:
            rarity = f"Common | + 1 {item_type}"
            item_strenght = 1
        
        print(f"a chest.\nInside the chest you find a {item_choice} with a rarity of: {rarity}")

        if item_type == "STR":
            if len(adventurer.inventory) == 5:
                adventurer.inventory_full(item_choice)
            else:
                adventurer.strenght(item_strenght)
                adventurer.chest(item_choice, rarity)
        else:
            adventurer.potion(item_choice, rarity)


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



def monster_hp_calculation():
    health = random.randint((-4 + adventurer.properties[1]), (1 + adventurer.properties[1])) # Keeping the chances the same
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

story_printing(f"Welcome to the Hall of Beasts, {adventurer.name}", 0.1)


# While Loop
while True:    
    door_choice = input("""What's your choice?\n[A] Door 1 (To the left)\n[B] Door 2 (Forward)\n[C] Door 3 (To the right)\n[D] See adventurer stats\n[E] See adventurer inventory\n[F] See/Use Potions\n> """).lower()

    door_choice_result = random.randint(1, 101) # Changing ods to %

    if door_choice == "a":
        print(f"You open door 1 and found", end=" ")
    
    elif door_choice == "b":
        print(f"You open door 2 and found", end=" ")
    
    elif door_choice == "c":
        print(f"You open door 3 and found", end=" ")

    elif door_choice == "d":
        print(f"""Current HP: {adventurer.properties[0]}\nCurrent STR: {adventurer.properties[1]}\nCurrent LVL: {adventurer.properties[2]}\n""")
        continue
    
    elif door_choice == "e":
        item.inventory()
        continue

    elif door_choice == "f":
        pass # FIXAR SENARE

    else:
        print("ERROR! Invalid input, please try again.")
        continue
    
    if door_choice_result <= 10:
        adventurer.trap(1)

    elif door_choice_result <= 50:
        item.chest()
        
    elif door_choice_result <= 100:
        monster_health = monster_hp_calculation()
        adventurer.monster(monster_health)

        
    else:
        print("ERROR! Invalid input, please try again.") 
        continue 
    
    if adventurer.properties[0] <= 0:
        print("You have reached 0 HP and died!")
        quit()

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
        damage_ods = random.randint(1, 101)
        final_boss.damage(damage_ods)

    elif BOSS_fight_action =="b":
        Block_ods = random.randint(1,101)
        final_boss.stunned(Block_ods)
    
    elif BOSS_fight_action =="c":
        Dodge_ods = random.randint(1,101)
        final_boss.dodge(Dodge_ods)
        
    else:
        print("Error! Invalid input, please try again.")
        continue
        
    '''elif BOSS_fight_action == "d":
        if item.potion >= 1:
            adventurer.properties[0] += 1
            item.potion -= 1            
            print("You drank a potion and gained HP")
            print(f"You now have {adventurer.properties[0]} HP")
            continue
        elif item.potion < 1:
            print("oh,no! You have no more potions. You have to make another choice")
            continue''' # ADD THIS ABOVE ONCE FINISHED WORKING ON IT.
